"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Hamid Khan
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Value      : {value:>5.2f}")
    print(f"Limit      : {limit:>5.2f}")
    print(f"Difference : {difference:>5.2f}")
    print(f"Percent    : {percent:>5.2f}%")
    print(f"Status     : {status}")
    print("=" * 34)
# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

# records = []   # replace with your code

def load_records(path):
    records = []
    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)})

    return records

records = load_records("records_sample.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

count = 0

for record in records:
    difference, percent, status = check_record( record["value"],
                                                record["limit"])

    print_report(
        record["label"],record["value"],
        record["limit"], difference,
        percent, status)

    if status == "OVER LIMIT":
        count += 1

print(f"Total records OVER LIMIT: {count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
