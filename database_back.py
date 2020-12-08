#!/usr/bin/python

import mysql.connector
import os
import time
import pipes
import datetime

print(os.getcwd())
host="localhost"
user="root"
password="satwik@15160521"
database='/Users/hp/bckp/name.txt'

backup_path='/bckp'

DateT=time.strftime('%Y%m%d-%H%M%S')

today_path=backup_path+'/'+DateT


try:
    print("Checking Directory status")
    os.stat(today_path)
except:
    os.mkdir(today_path)
    print("Directory Created")

    
print ("checking for databases names file.")
if os.path.exists(database):
    file1 = open(database)
    multi = 1
    print ("Databases file found...")
    print ("Starting backup of all dbs listed in file " + database)
else:
    print ("Databases file not found...")
    print ("Starting backup of database " + database)
    multi = 0
 

if multi:
   in_file = open(database,"r")
   flength = len(in_file.readlines())
   print(flength)
   in_file.close()
   p = 1
   dbfile = open(database,"r")
 
   while p <= flength:
       db = dbfile.readline()
       print("file name --->"+db)
       db = db[:-1]
       os.chdir("/Program Files/MySQL/MySQL Server 8.0/bin")
       dumpcmd = "mysqldump -h" +host + " -u" + user + " -p" + password + " " + db + " > " + pipes.quote(today_path) + "/" + db + ".sql"
       os.system(dumpcmd)
       gzipcmd = "gzip " + pipes.quote(today_path) + "/" + db + ".sql"
       os.system(gzipcmd)
       p = p + 1
   dbfile.close()
else:
   db = database
   dumpcmd = "mysqldump --routines -h " + host + " -u " + user + " -p" + password + " " + db + " > " + pipes.quote(today_path) + "/" + db + ".sql"
   os.system(dumpcmd)
   gzipcmd = "gzip " + pipes.quote(today_path) + "/" + db + ".sql"
   os.system(gzipcmd)
 
print ("")
print ("Backup script completed")
print ("Your backups have been created in '" + today_path + "' directory")
 
