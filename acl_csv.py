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
    csv_file_name = acl_file_name[:-4]+"_.csv"
    with open(acl_file_name,'r') as f:
        for row in f:
            row_csv = row[:-1].split(' ')
            if len(sys.argv) == 3:
                csv = sys.argv[2]
            else:
                csv = "0"
            for c in range(2,9):
                if c == 1:
                    csv = csv + add_permit(int(row_csv[c]))
                else:
                    csv = csv + "," + row_csv[c]
            print(csv)
main()
