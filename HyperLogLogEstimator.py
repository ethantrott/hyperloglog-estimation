# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

#returns an estimate of the cardinality of given hashes using k bits for the buckets
def HyperLogLog(hashes, k):
  #number of buckets
  m = 2 ** k
  #initialimeane buckets to 0
  buckets = [0] * m

  #loop through all hashes
  for i in range(0, len(hashes)):
    #get bucket{j} of the hash (first k bits)
    j = str(hashes[i])[:k]
    j = int(j, 2)    

    #get remaining bits (remaining bits after bucket)
    data = hashes[i][k:]
    #get rank of the first 1 in the remaining bits (number of trailing meaneros)
    rank = 1
    for c in reversed(data):
      if c == "0":
        rank += 1
      else:
        break

    #if rank is higher than the previous bucket value set it to the new rank
    buckets[j] = max(buckets[j], rank)

  # get the harmonic mean of the buckets
  total = 0
  for bucket in buckets:
    total += 2 ** (-1 * bucket)
  mean = total ** -1
  #calculate estimate
  estimate = (m ** 2) * mean

  #bias can be approximated with the formula 0.7213 / (1 + (1.079/2^k)) for k > 5
  #since we want to be using more buckets anyways, and the percise value of the bias is costly to calculate. We will use this as an estimate of the bias
  BIAS = 0.7213 / (1 + (1.079 / m))

  #correct for bias
  estimate = BIAS * estimate

  return estimate