# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:34:36 2019

@author: 99993
"""

def read_bills():
    bills = []
    bills_file = open('bills.csv')
    for line in bills_file:
        if len(line) > 1:
            bills.append(line.strip().split(','))
            bills[-1][-1] = bills[-1][-1].strip()
    return bills

