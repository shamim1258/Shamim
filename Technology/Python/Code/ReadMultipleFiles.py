import os
import csv
path="C://Users//khan530//Desktop//Docs//AWS//S3 Bucket Prod//new"
#for x in os.listdir():
for x in os.walk(path):
    #print("Get file::",x[2])
    files_list = x[2]
    for file in files_list:
        if file.endswith('.csv'):
        #with open(file) as read_file:
            read_file = open(file)
            next(read_file)
            #reader = csv.reader(read_file, delimiter=';')
            print(read_file.read())

