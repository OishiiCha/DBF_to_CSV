import csv, os
from dbfread import DBF
from os import walk

directory = input('Directory: ')

files = []
for (dirpath, dirnames, filenames) in walk(directory):
    files.extend(filenames)
    break

DBFfiles = []

for i in range(len(files)):
    x = files[i-1]
    if '.dbf' in x or '.DBF' in x:
        DBFfiles.append(x)

for i in range(len(DBFfiles)):
    strlen = len(DBFfiles[i-1])
    oldFileName = DBFfiles[i-1]
    newFileName = str(oldFileName[0:strlen-4]+'.csv')
    print('File: %s of %s, Old Name: %s, New Name: %s' % (i,len(DBFfiles),oldFileName,newFileName))
    with open(directory + '/' + DBFfiles[i-1], newline='') as infile, open(directory + '/' + newFileName, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=';')
        for row in reader:
            writer.writerow(row)
