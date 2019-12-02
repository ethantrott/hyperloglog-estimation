import csv

# this variable allows us to limit the number of rows we parse
# (for convenience in debugging)
row_limit = -1

# returns the total number of rows in the file
def count_lines(filename):
    with open(filename, "r") as csvfile:
        return sum(1 for row in csvfile) - 1

# this will yield each Plate ID within our row_limit when iterated over
def get_plates(filename):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        count = -1
        for row in datareader:
            if (count == -1):
                #ignore the header row
                count += 1
            elif (row_limit == -1 or count < row_limit):
                yield row[1]
                count += 1
            else:
                return