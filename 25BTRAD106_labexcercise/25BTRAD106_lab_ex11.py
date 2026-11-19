# Lab 11: Log file reader program
import os

filename = "app.log"

# Create a sample log file for demonstration
with open(filename, "w") as f:
    f.write("INFO: Application started\n")
    f.write("INFO: User logged in\n")
    f.write("WARNING: Disk space low\n")
    f.write("ERROR: Database connection failed\n")
    f.write("INFO: Retrying connection\n")
    f.write("ERROR: Timeout occurred\n")

# Read and count
if not os.path.exists(filename):
    print("Error: File not found")
elif os.path.getsize(filename) == 0:
    print("The log file is empty")
else:
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    with open(filename, "r") as f:
        for line in f:
            for keyword in counts:
                if keyword in line:
                    counts[keyword] += 1

    print("Log Summary")
    for keyword, total in counts.items():
        print(keyword, ":", total)
