import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

for record in csvfile:
    print('ID: ', record [0])
    print('Fname: ', record [1])
    print('Lname: ', record [2])
    print(record [3])
    print(record [4])
    print(record [5])

    input = ()

