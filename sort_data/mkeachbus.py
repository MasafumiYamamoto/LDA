import csv
import os

#os.mkdir("business")
ifile=open("nNVrevtopic_LDA.csv","r")
idata=csv.reader(ifile)
idata.next()
for line in idata:
    wfile=open("business/"+line[1],"ab")
    writer=csv.writer(wfile)
    writer.writerow(line)

ifile.close()
wfile.close()
