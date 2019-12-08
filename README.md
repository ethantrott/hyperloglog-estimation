# The Evolution of the HyperLogLog Estimator
 python implementations of Flajolet-Martin, LogLog, SuperLogLog, and HyperLogLog estimation algorithms, used to estimate the cardinality of unique traffic violations in NYC in the 2019 fiscal year

## the dataset (nyc-dataset.csv)
 the dataset is a set of all recorded traffic violations in New York City during the 2019 fiscal year (August 2018 - June 2019). It contains a lot of information, but we will only be looking at the Plate ID, in order to estimate the number of unique offenders. **the dataset can be downloaded [here](https://data.cityofnewyork.us/api/views/faiq-9dfq/rows.csv?accessType=DOWNLOAD) (download and rename to "nyc-dataset.csv")**

## main.py  [example output](https://raw.githubusercontent.com/ethantrott/hyperloglog-estimation/master/images/example_output.png)
 This is the file you want to run. It gets the values returned by each of the estimators and compares the estimation times and accuracies of each. 

## ActualCount.py
 manually counts the number of unique offenders - this allows us to determine the accuracy of our approximations

## FlajoletMartinEstimator.py
 uses the Flajolet-Martin algorithm to approximate the unique entries in the dataset

## LogLogEstimator.py
 uses LogLog Estimation to approximate the number of unique entries in the dataset

## SuperLogLogEstimator.py
 uses SuperLogLog Estimation to approximate the number of unique entries in the dataset

## HyperLogLogEstimator.py
 uses HyperLogLog Estimation to to approximate the number of unique entries in the dataset
