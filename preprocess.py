#import numpy as np
import csv

reader = csv.reader(open("Table3.csv",'rb'), delimiter=",")
x = list(reader)

rows,cols = len(x),len(x[0])
print(rows)
print(cols)
for i in range(1,rows):
    for j in range(1,cols):
        try:
            k = str(x[i][j]).split('%')[0]
            print(k)
            k = k.strip("%")
            k = float(k)/100
            x[i][j] = str(k)
            print(k)
        except:
            print("Blank")
            
with open("Table3.csv','wb") as cf:
    writer = csv.writer(cf, delimiter=",")
    writer.writerows(x)
        
print(x)
        
