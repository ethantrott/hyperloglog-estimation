# The Evolution of the HyperLogLog Estimator
# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

import sys, os.path, time, statistics
import csv_parser, ActualCount
import FlajoletMartinEstimator, LogLogEstimator, SuperLogLogEstimator, HyperLogLogEstimator

# the file to parse for unique plates
filename = "nyc-dataset.csv"

# the number of bits to use in identifying buckets
# 2**ex_buckets = number of buckets
ex_buckets = 8

# number of runs to average with different hashes
loops_to_run = 8

print ("The Evolution of the HyperLogLog Estimator")
print ("by Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott\n")

# check if the Plate ID hashes have been generated before
# if so, load them. if not, create them
plate_hashes = []
if os.path.exists("hashes.csv"):
    print("Loading plate hashes from file..")
    plate_hashes = csv_parser.load_hashes()
else:
    # check to make sure the dataset has been downloaded and named properly
    if not os.path.exists(filename):
        print("Error: Please download the dataset from https://data.cityofnewyork.us/api/views/faiq-9dfq/rows.csv?accessType=DOWNLOAD and place it in this directory as "+filename)
        exit()
        
    print("Creating plate hashes.. (this may take a moment)")
    plate_hashes = csv_parser.create_hashes(filename)
print(str(len(plate_hashes))+" plate hashes loaded.\n")

# directly tally the number of unique plates
print("Calculating exact amount of unique plates..")
exact_unique = ActualCount.get_exact_unique_using_set(filename)
print("There are exactly "+str(exact_unique)+" unique plates..\n")

#run tests and store results
fm = []
ll = []
sll = []
hll = []
for i in range(0, loops_to_run):
    #print loading message
    sys.stdout.write("Running test " + str(i + 1) + " of " + str(loops_to_run) + ".. (this may take a moment)")
    sys.stdout.flush()

    #Generate test hashes
    hashes = []
    for hash in plate_hashes:
        #encode the hash in binary
        hash = '{:256b}'.format(int(hash, 16)).replace(' ','0')

        off = i*32
        temp = hash[len(hash)-(32+off)+1:len(hash)-off]
        hashes.append(temp)

    #approximate values and add to results array
    fm.append(FlajoletMartinEstimator.FlajoletMartin(hashes))
    ll.append(LogLogEstimator.LogLog(hashes, ex_buckets))
    sll.append(SuperLogLogEstimator.SuperLogLog(hashes, ex_buckets))
    hll.append(HyperLogLogEstimator.HyperLogLog(hashes, ex_buckets))

    #reset line
    sys.stdout.write('\r')

#test formatter
def printTest(label, expected, actual):
  #print header
  print('*'*50)
  print('{s:{c}^{n}}'.format(s=f' {label} ', n=50, c='*'))
  print('*'*50)
  print()

  #print results
  print('{s:{c}^{n}}'.format(s=' Expected result ', n=50, c='-'))
  print(expected)
  print('{s:{c}^{n}}'.format(s=' Actual results ', n=50, c='-'))
  print("\n".join("{0:.0f}".format(x) for x in actual))
  print('{s:{c}^{n}}'.format(s=' Mean result ', n=50, c='-'))
  print("{0:.0f}".format(statistics.mean(actual)))
  print()
  
  #print statistics
  print('{s:{c}^{n}}'.format(s=' Difference ', n=50, c='-'))
  print("{0:.0f}".format(expected - statistics.mean(actual)))
  print('{s:{c}^{n}}'.format(s=' Percent Error ', n=50, c='-'))
  print("{0:.2%}".format(abs(expected - statistics.mean(actual)) / expected))
  print('{s:{c}^{n}}'.format(s=' Standard Deviation ', n=50, c='-'))
  print("{0:.0f}".format(statistics.pstdev(actual)))
  print()
  print()

#print results
printTest("Flajolet-Martin", exact_unique, fm)
printTest("LogLog", exact_unique, ll)
printTest("SuperLogLog", exact_unique, sll)
printTest("HyperLogLog", exact_unique, hll)