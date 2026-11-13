"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

#df = None   # replace with pd.read_csv("your_file.csv")
#%%
import pandas as pd

df = pd.read_csv("record_sample_t.txt")

print(df)
#%%
# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".
# your column(s) go here

#%%
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK")
print(df)
#%%
# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

# ================================================================= OUTPUT
#%%

print("\n DATAFRAME")
print(df)
print("\nRECORDS THAT ARE NOT OK")
print(df[df["status"] != "OK"])
print("\nCOUNT PER GROUP STATUS")
counts = df.groupby("status").size()
print(counts)

df.to_csv("record_results.csv", index=False)

import matplotlib.pyplot as plt

counts.plot(kind="bar", color="silver")

plt.title("Count of Records per Status")
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()

plt.savefig("status_chart.png")
plt.show()
#%%
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
