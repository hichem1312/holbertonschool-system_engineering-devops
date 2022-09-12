#!/usr/bin/python3
'''Get some data from API'''


from requests import get
import requests
from sys import argv
import csv

if __name__ == "__main__":
    '''module'''
    t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    t = t.json()
    us = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    us = us.json()
    u = us["username"]
    f = open('./{}.csv'.format(argv[1]), 'w')
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    for i in t:
        if (((i["userId"]) == int(argv[1]))):
            wr.writerow([str(
                i["userId"]), u, i["completed"], i["title"]])
    f.close()
