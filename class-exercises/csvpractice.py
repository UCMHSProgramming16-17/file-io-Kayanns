# import module 

import csv 

#create a file

csvfile2 = open('practicecsv' , 'w' )

#create csvwriter

csvwriter2 = csv.writer(csvfile2, delimiter=',')

#write information

csvwriter2.writerow([1, 2, 3])

csvwriter2.writerow(['Mandy', 'shefali', 'sidney'])

csvwriter2.writerow(['green' , 'black' , 'red'])

csvwriter2.writerow(['$6.99' , '$1.99' , '$3.99'])

csvwriter2.writerow(['paid' , 'not paid' , 'paid half'])

