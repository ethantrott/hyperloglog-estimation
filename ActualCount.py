import csv_parser, time

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

def get_unique_using_sort(filename):
    #to sort we must load all entries into an array
    print("Loading data into array..")
    start = time.time()

    entries = []
    csv_parser.fill_array_with_plates(filename, entries)

    time_used = time.time() - start
    print (str(len(entries))+ " entries loaded in "+str(time_used)+" seconds")
    
    start = time.time()
    sorted_entries = sorted(entries)
    time_used = time.time() - start
    print (str(len(sorted_entries))+ " entries sorted in "+str(time_used)+" seconds")
    with open("sorted.csv", "w") as txt_file:
        for line in sorted_entries:
            txt_file.write(line + "\n")
    
    # TODO: go through sorted array to see if there are duplicates, if so remove, then count