import csv_parser, ActualCount

#the file to parse for unique plates
filename = "nyc-dataset.csv"

# count the total number of traffic violations
print("Counting the total number of traffic violations..")
## TODO uncomment this line (it's just commented to save time)
#total_entries = csv_parser.count_lines(filename)
total_entries = 11467506
print(str(total_entries) + " entries in " + filename)

# directly tally the number of unique plates
print("Counting unique plates...")
actual_unique = ActualCount.count_all_unique_plates(filename, total_entries)
print(str(actual_unique) + " unique plates counted.")