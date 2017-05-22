# -*- coding: utf-8 -*-
#%!/bin/bash python3
import sys
import csv

def add_acl():
    pass

def add_permit(permit):
    if permit == 0:
        return permit
    if permit == 1:
        return deny

def main():
    acl = "access-list"
    csv_file_name = sys.argv[1]
    acl_file_name = csv_file_name[:-4]+"_acl.txt"
    print(acl_file_name)
    with open(csv_file_name,'r') as f:
        reader = csv.reader(f)

        for row in reader:
            for c in range(1,8):
                print(row[c])

main()
