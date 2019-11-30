import csv_parser, time

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