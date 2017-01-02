# import module

import csv

#create file

filecsv = open('filetest.csv' , 'w')

# create csvwriter

csvwriter = csv.writer(filecsv, delimiter=',')

# write information

csvwriter.writerow(['Hello', 'i must seem very tired', 'it is because', 'i didnt get enough sleep'])

#close file

filecsv.close()