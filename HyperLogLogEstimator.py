# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

#returns an estimate of the cardinality of values using k bits for the buckets
def HyperLogLog(values, k):
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

  # get the harmonic mean of the buckets
  # harmonic mean{z} = 1 / sum(2 ^ -buckets)
  total = 0
  for bucket in buckets:
    total += 2 ** (-1 * bucket)
  z = total ** -1
  
  #calculate estimate
  estimate = (m ** 2) * z

  #this is an algebraic approximation for the bias dependant on the number of buckets
  bias = 0.7213/(1+1.079/m)

  #correct for bias
  estimate = bias * estimate

  return estimate