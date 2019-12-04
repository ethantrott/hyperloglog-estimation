# LogLog, SuperLogLog, and HyperLogLog Demo
# Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott
# COS226 University of Maine

import os.path, time
import csv_parser, ActualCount, LogLogEstimator, SuperLogLogEstimator, HyperLogLogEstimator

# the file to parse for unique plates
filename = "nyc-dataset.csv"

# the number of bits to use in identifying buckets
# 2**ex_buckets = number of buckets
ex_buckets = 8

print ("LogLog, SuperLogLog, and HyperLogLog Demo")
print ("by Dawsin Blanchard, Sam Braga, Brian Couture, and Ethan Trott\n")

# check to make sure the dataset has been downloaded and named properly
if not os.path.exists(filename):
    print("Error: Please download the dataset from https://data.cityofnewyork.us/api/views/faiq-9dfq/rows.csv?accessType=DOWNLOAD and place it in this directory as "+filename)
    exit()


# count the total number of traffic violations
print("Counting the total number of traffic violations..")
start = time.time()
total_entries = csv_parser.count_lines(filename)
time_used = time.time() - start
print("There are " + str(total_entries) + " entries in " + filename + ", counted in "+str(time_used) +" seconds\n")

# directly tally the number of unique plates
print("Calculating exact amount of unique plates..")
start = time.time()
exact_unique = ActualCount.get_exact_unique_using_set(filename)
time_used = time.time() - start
print ("There are exactly " + str(exact_unique)+ " unique plates, counted in "+str(time_used)+" seconds\n")

# approximate number of plates using LogLog Estimation
print("Approximating amount of unique plates using LogLog..")
start = time.time()
loglog_appx = LogLogEstimator.LogLog(csv_parser.get_plates(filename), ex_buckets)
time_used = time.time() - start
percent_error = abs(loglog_appx - exact_unique) / exact_unique * 100
print ("LogLog Estimation: " + str(loglog_appx)+ " unique plates, approximated in "+str(time_used)+" seconds")
print ("Percent Error: " + str(percent_error) + "% \n")

# approximate number of plates using SuperLogLog Estimation
print("Approximating amount of unique plates using SuperLogLog..")
start = time.time()
sloglog_appx = SuperLogLogEstimator.SuperLogLog(csv_parser.get_plates(filename), ex_buckets)
time_used = time.time() - start
percent_error = abs(sloglog_appx - exact_unique) / exact_unique * 100
print ("SuperLogLog Estimation: " + str(sloglog_appx)+ " unique plates, approximated in "+str(time_used)+" seconds")
print ("Percent Error: " + str(percent_error) + "% \n")

# approximate number of plates using HyperLogLog Estimation
print("Approximating amount of unique plates using HyperLogLog..")
start = time.time()
hloglog_appx = HyperLogLogEstimator.HyperLogLog(csv_parser.get_plates(filename), ex_buckets)
time_used = time.time() - start
percent_error = abs(hloglog_appx - exact_unique) / exact_unique * 100
print ("HyperLogLog Estimation: " + str(hloglog_appx)+ " unique plates, approximated in "+str(time_used)+" seconds")
print ("Percent Error: " + str(percent_error) + "% \n")