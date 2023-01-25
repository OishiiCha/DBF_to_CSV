import csv, os, sys
from os import walk


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#directory = input('Directory: ')
def main(argv):
    argnum = len(argv)
    directory = argv[0]
    newdirectory = directory + '/NWScheduleImports'
    if os.path.exists(directory):
        os.system('mkdir ' + newdirectory)
    else:
        print(f'{bcolors.FAIL}Directory does not exist!{bcolors.ENDC}')


    files = []
    DBFfiles = []

    for (dirpath, dirnames, filenames) in walk(directory):
        files.extend(filenames)
        break

    for i in range(len(files)):
        x = files[i-1]
        if '.dbf' in x or '.DBF' in x:
            DBFfiles.append(x)

    for i in range(len(DBFfiles)):
        strlen = len(DBFfiles[i-1])
        oldFileName = DBFfiles[i-1]
        newFileName = str(oldFileName[0:strlen-4]+'.csv')
        print(f'{bcolors.UNDERLINE}File: %s of %s{bcolors.ENDC}, Old Name: {bcolors.OKCYAN}%s{bcolors.ENDC}, New Name: {bcolors.OKGREEN}%s{bcolors.ENDC}' % (i+1,len(DBFfiles),oldFileName,newFileName))
        with open(directory + '/' + DBFfiles[i-1], newline='') as infile, open(newdirectory + '/' + newFileName, 'w', newline='') as outfile:
            reader = csv.reader(infile, delimiter=',')
            writer = csv.writer(outfile, delimiter=';')
            for row in reader:
                writer.writerow(row)

if __name__ == '__main__':
    main(sys.argv[1:])

