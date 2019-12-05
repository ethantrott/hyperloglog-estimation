# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

import hashlib

#returns an estimate of the cardinality of values using k bits for the buckets
def HyperLogLog(hashes, off, k):
  #number of buckets
  m = 2 ** k
  #initialize buckets to 0
  buckets = [0] * m

  #loop through all hashes
  for hash in hashes:
    #encode the hash in binary
    hash = '{:256b}'.format(int(hash, 16)).replace(' ','0')
    
    temp = hash[len(hash)-(32+off)+1:len(hash)-off]

    #get bucket{j} of the hash (first k bits)
    j = temp[:k]
    j = int(j, 2)

    #get remaining bits after bucket
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

  # get the harmonic mean of the buckets
  # harmonic mean{z} = 1 / sum(2 ^ -buckets)
  total = 0
  for bucket in buckets:
    total += 2 ** (-1 * bucket)
  z = total ** -1

  #calculate estimate
  estimate = (m ** 2) * z

  #bias can be approximated with the formula 0.7213 / (1 + (1.079/2^k)) for k > 5
  #since we want to be using more buckets anyways, and the percise value of the bias is costly to calculate. We will use this as an estimate of the bias
  BIAS = 0.7213 / (1 + (1.079 / m))

  #correct for bias
  estimate = BIAS * estimate

  return estimate

#find the average estimate for n different offsets of the hash with k bits for buckets
def average_with_different_hashes(hashes, k, n):
  total = 0
  for i in range(n):
    total += HyperLogLog(hashes, i*32, k)
  return total/n