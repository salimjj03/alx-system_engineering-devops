#!/usr/bin/python3
""" This module using this REST API,
for a given employee ID, returns information
about his/her TODO list progress. """

import requests
import sys

query1 = {"id": sys.argv[1]}
query = {"userId": sys.argv[1]}


if __name__ == "__main__":

    with requests.get(
            "https://jsonplaceholder.typicode.com/users",
            params=query1
            ) as result1:
        pass
    with requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params=query
            ) as result:
        total = len(requests.get(
            "https://jsonplaceholder.typicode.com/todos"
            ).json())
        ls = result.json()
        print("Employee {} is done with tasks({}/{})".format(
            result1.json()[0].get("name"),
            len(ls),
            total
            ))
        for i in ls:
            print("\t {}".format(i.get("title")))
