# hyperloglog estimation
 python implementations of LogLog, SuperLogLog, and HyperLogLog, used to estimate the cardinality of unique traffic violations in NYC in the 2019 fiscal year

## the dataset (nyc-dataset.csv)
 the dataset is a set of all recorded traffic violations in New York City during the 2019 fiscal year (August 2018 - June 2019). It contains a lot of information, but we will generally only be looking at the Plate ID, in order to estimate the number of unique offenders. **the dataset can be downloaded [here](https://data.cityofnewyork.us/api/views/faiq-9dfq/rows.csv?accessType=DOWNLOAD) (download and rename to "nyc-dataset.csv")**

## LogLogEstimator.py
 uses the LogLog algorithm to return the estimate of unique offenders in the dataset

## SuperLogLogEstimator.py
 uses the SuperLogLog algorithm to return the estimate of unique offenders in the dataset

## HyperLogLogEstimator.py
 uses the HyperLogLog algorithm to return the estimate of unique offenders in the dataset

## ActualCount.py
 goes through and manually counts the number of unique offenders, in order to determine the accuracy of the estimations

## main.py
 gets the values returned by each of the estimators and compares the estimation times and accuracies of each. this is the file you want to run.
