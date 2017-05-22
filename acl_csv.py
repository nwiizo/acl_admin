# -*- coding: utf-8 -*-
#%!/bin/bash python3

import sys

def add_acl():
    pass

def add_permit(permit):
    if permit == "permit":
        return ",0"
    if permit == "deny":
        return ",1"

def main():
    acl_file_name = sys.argv[1]
    csv_file_name = csv_file_name[:-4]+"_.csv"
    with open(acl_file_name,'r') as f:
        reader = csv.reader(f)

        for row in reader:
            acl = "access-list"
            for c in range(1,9):
                if c == 1:
                    acl = acl + add_permit(int(row[c]))
                else:
                    acl = acl + " " + row[c] 
            print(acl)
main()
