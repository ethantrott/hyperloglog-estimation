# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

import math

#returns an estimate of the cardinality of values using k bits for the buckets
def SuperLogLog(values, k):
  #number of buckets
  m = 2**k
  #initialize buckets to 0
  buckets = [0] * m

  #loop through all values
  for value in values:
    #get 32 bit hash of the value
    temp = '{:032b}'.format(hash(value))

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
  
  #calculate lower and upper cutoffs
  #a cut off of ~0.7 is optimal
  cutoff = 0.7
  lower = math.floor(cutoff * m)
  upper = m - lower

  #apply cutoff
  for i in range(upper):
    buckets.remove(max(buckets))

  #get bucket average
  average = sum(buckets) / lower
  #calculate estimate
  estimate = m * 2 ** average

  #bias converges to 0.7213 for larger numbers of buckets (k > 5)
  #since we want to be using more buckets anyways, and the percise value of the bias is costly to calculate. We will use this convergance as an estimate of the bias
  BIAS = 0.7213
  #correct for bias
  estimate = BIAS * estimate

  return estimate