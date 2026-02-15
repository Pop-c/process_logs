
#Scenario:
#You need to generate a report from a legacy RADIUS accounting server. The server dumps
#usage logs into massive text files.
#● Input: A text file where each line is: TIMESTAMP,USER_ID,DATA_USAGE_KB
#● Constraint: The log file is 10GB, but your script must run on a micro-instance with only
#512MB RAM.
#Your Task:
#Write a Python script that:
#1. Reads the file safely (without crashing from Out-Of-Memory errors).
#2. Aggregates the total data usage per user.
#3. Prints the Top 5 Users by total usage.
#Starter Code:

import sys
import random
import heapq
import collections
LOG_FILE = "radius_logs.txt"
def process_logs(file_path):
    """
    TODO: Read file, aggregate usage, print top 5 users.
    Constraint: Memory efficient (Stream the file).
    """
    agg_users = {} # key: user_id => val: tot_process_data
    with open(file_path, 'r') as f:
        for line in f:
            time_stamp, user_id, data_use = line.split(",")
            data_use = int(data_use) 
            if agg_users and user_id in agg_users:
                agg_users[user_id] = agg_users[user_id] + data_use
            else:
                agg_users[user_id] =  data_use #firs val
           
            
        #sort sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        agg_users = dict(sorted(agg_users.items(), key=lambda item:item[1], reverse=True))
        count = 0
        for key,val in agg_users.items():
            if count == 5:
                break
            print( key)
            count += 1

    pass
# --- Helper: Generate Dummy Data (Run this once) ---
def generate_dummy_file(filename, lines=50000):
    """ Creates a dummy log file for testing purposes. """
    print(f"Generating {lines} lines of test data...")
    users = [f"user_{i}" for i in range(1, 101)] # 100 unique users
    with open(filename, 'w') as f:
        for _ in range(lines):
            ts = 1678886400 + random.randint(0, 86400)
            user = random.choice(users)
            kb = random.randint(10, 5000)
            f.write(f"{ts},{user},{kb}\n")
            print("Done. File created.\n")
        
if __name__ == "__main__":
    # 1. Create the dummy file locally
    generate_dummy_file(LOG_FILE)
    # 2. Run your processing function
    print("--- Starting Processing ---")
    process_logs(LOG_FILE)