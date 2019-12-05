# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

import hashlib

#returns an estimate of the cardinality of values using k bits for the buckets
def LogLog(hashes, off, k):
  #number of buckets
  m = 2**k
  #initialize buckets to 0
  buckets = [0] * m

  #loop through all hashes
  for hash in hashes:
    #encode the hash in binary
    hash = bin(int(hash, 16))

    temp = hash[len(hash)-(32+off):len(hash)-off]

    #get bucket{j} of the hash (first k bits)
    j = temp[:k]
    j = int(j, 2)

    #get remaining bits (remaining bits after bucket)
    data = temp[k:32]
    #get rank of the first 1 in the remaining bits (number of trailing zeros)
    rank = 1
    for c in reversed(data):
      if c == "0":
        rank += 1
      else:
        break

    #if rank is higher than the previous bucket value set it to the new rank
    buckets[j] = max(buckets[j], rank)
  
  #get bucket average
  average = sum(buckets) / m
  #calculate estimate
  estimate = m * 2 ** average

  #bias converges to 0.79402 for larger numbers of buckets (k > 5)
  #since we want to be using more buckets anyways, and the percise value of the bias is costly to calculate. We will use this convergance as an estimate of the bias
  BIAS = 0.397011808
  #correct for bias
  estimate = BIAS * estimate

  return estimate

#find the average estimate for n different offsets of the hash with k bits for buckets
def average_with_different_hashes(hashes, k, n):
  total = 0
  for i in range(n):
    total += LogLog(hashes, i*32, k)
  return total/n