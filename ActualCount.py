import time
import csv_parser

# this function is O(n^2). this would take a *very* long time to run on our dataset
# we will not use this, except for subsets
def count_all_unique_plates(filename, total_entries):
    start = time.time()

    total_count = 0
    next_percent = 0.01
    unique = []

    for plate in csv_parser.get_plates(filename):
        if plate not in unique:
            unique.append(plate)
        
        total_count += 1
        if (total_count / total_entries > next_percent):
            time_used = time.time() - start
            print("    " + str(int(next_percent*100)) + "% of entries parsed in "+str(time_used)+" seconds. ("+str(len(unique))+" unique)")
            next_percent += 0.01

    return len(unique)

#determine the exact amount of unique elements using set() to remove duplicates
#this is **much** faster than count_all_unique_plates()
def get_exact_unique_using_set(filename):
    #to sort we must load all entries into an array
    entries = []
    csv_parser.fill_array_with_plates(filename, entries)

    #use set() to remove duplicates
    entries = set(entries)

    #return the number of elements that aren't duplicates
    return len(entries)

