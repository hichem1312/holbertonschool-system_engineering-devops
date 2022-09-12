#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv

if __name__ == "__main__":
    '''module'''
    all_list = []
    a = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    a = a.json()
    b = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    b = b.json()
    x = 0
    y = 0
    for i in a:
        if ((i["userId"]) == int(argv[1])):
            x += 1
            if (i["completed"]):
                y += 1
                all_list = all_list + [(i["title"])]
     print("Employee {} is done with tasks({}/{}):".format(b["name"], y, x))
     for i in all_list:
         print("\t", i)
