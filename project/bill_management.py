# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:34:36 2019

@author: 99993
"""
def read_bills():
    return [[col.strip() for col in row.strip().split(',')]
             for row in open('bills.csv') if len(row) > 1]

def write_bills(bills):
    bill_file = open('bills.csv', 'w')
    for bill in bills:
        bill_file.write(', '.join(bill) + '\n')

def get_message():
    return 'Hello, Welcome to the Bill Management Company\n' + \
        '1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit'

def display_menu():
    print(get_message())

def view_bills(bills):
    for bill in bills:
        print(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])
    
def process_choice(bills):
    choice = input('Please enter an option:')
    while choice != '5':
        if choice == '1':
            view_bills(bills)
        elif choice == '4':
            print('The terms of the billing management company')
        choice = input('Please enter an option:')

def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    write_bills(bills)
    
if __name__ == '__main__':
    main()
