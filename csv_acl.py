# -*- coding: utf-8 -*-
#%!/bin/bash python3
import sys
import csv

def add_acl():
    pass

def add_permit(permit):
    if permit == 0:
        return " permit"
    if permit == 1:
        return " deny"

def main():
    csv_file_name = sys.argv[1]
    acl_file_name = csv_file_name[:-4]+"_acl.txt"
    with open(csv_file_name,'r') as f:
        reader = csv.reader(f)

        for row in reader:
            acl = "access-list"
            for c in range(1,len(row)):
                if c == 1:
                    acl = acl + add_permit(int(row[c]))
                else:
                    acl = acl + " " + row[c] 
            print(acl)
main()
