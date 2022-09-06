import csv

infile = open('customer_country.csv', 'r')

for record in infile:

    infile = open('customer_country.csv', 'w')
    infile.write('Fname:   ' +'Lname:   ' + 'Country: ') 
    infile.write(record [1] + record [2] + record [4] )
    
    infile.close()
