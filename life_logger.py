import time
import sys
import os
import csv
import JournEntry

def file_search():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory: %s" %dirName)
        for fname in fileList:
            print("\t%s" %fname)

def print_journal(journal):
    for entry in journal:
        print(entry)

def display_entries():
    print("Give me a second to collect your logs...")
    jour_file = csv.reader(open("journal.csv",'r'))
    journal = []
    for line in jour_file:
        if line != [] and line[0] != '#':
            # line = line.split(',')
            _id = line[0]
            _date = line[1]
            _time = line[2]
            _header = line[3]
            _body = line[4]
            _tags = line[5]
            journal.append(JournEntry.Jentry(_id,_date,_time,_header,_body,_tags))
    print_journal(journal)

def log_entry():
    print("Alright, tell us about your day.")
    rand_id = 1
    date = input("Date: ")
    new_time = time.strftime("%I:%M:%S")
    head = input("Entry Header: ")
    body = input("Body: ")
    tags = '|'.join(input("Tags: ").split(","))
    if date == '':
        date = time.strftime("%m/%d/%Y")

    new_entry = JournEntry.Jentry(rand_id, date, new_time, head, body, tags)
    new_entry.write_entry_to_file()
    print('New entry was successfully created!')
    print(date)

def clear_file():
    file = open('journal.csv','w')
    file.close()

def process_command(command):
    if command == 'log':
        log_entry()
    elif command == 'disp':
        display_entries()
    elif command == 'cls':
        if input("Are you sure? (y or n)") == 'y':
            if input("Are you really sure? (y or n)") == 'y':
                if input("Are you really really sure? (y or n)") == 'y':
                    clear_file()

def get_command():
    print("Please enter a command:")
    print("\tlog  ->  make a new entry")
    print("\tdisp ->  display previous journal entries")
    print("\tcls  ->  clear your entire journal (not reversible)")
    print("\texit ->  exit Life Logger")
    command = ''
    while command != 'exit':
        print()
        command = input("-> ").lower()
        process_command(command)

def main():
    print("Welcome to your personal journal")
    print("--------------------------------------")
    get_command()

main()
