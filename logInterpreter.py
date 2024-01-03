import re
import time as t
f= open("file.log" , "r")
new = f.read()
f.close()
new = new.split("PrintBatchStatsToLog")
i = 2
stripped = []

while i< len(new):
    stripped.append((new[i].replace(" - Totals: ", "")).split("\n")[0])
    i+=3
# stripped value : Transaction Count: 193, Images Count: 782, Images Found: 782, Images Not Found: 0,  DB Fetch (ms): 291, Finding Images (ms): 5154, DB Save (ms): 971. Batch Total Time (s): 2

f = open("file.txt", "a")


f.write("Transaction count, Images Count, Images found, Images Not found, DB Fetch (ms), Finding Images(ms), DB Save (ms), Batch Total Time\n")
for i in range(len(stripped)):
    values = re.split("(?<=:)(.*?)(?=,)", stripped[i]) #gets value between : and ,  
    f.write(values[1].strip() + "," + values[3].strip() + "," +values[5].strip() + "," +values[7].strip() + "," +values[9].strip() + "," +values[11].strip() + "," + values[12].split(":")[1].split(".")[0].strip() + "," +values[12].split(":")[2].strip() + "\n")
f.close()

"""
KEY
1: Transaction count
2: Images Count
3: Images found
4: Images Not found
5: DB Fetch (ms)
6: Finding Images(ms)
7: DB Save (ms)
8: Batch Total Time

def listToString(s):
    str1 = " "
    return (str1.join(s))
stripped = listToString(stripped)
"""