# process_logs
You need to generate a report from a legacy RADIUS accounting server. The server dumps usage logs into massive text files.

## Requirements 
-  Write a Python script that:
-  Reads the file safely (without crashing from Out-Of-Memory errors).
-  Aggregates the total data usage per user.
-  Prints the Top 5 Users by total usage.
