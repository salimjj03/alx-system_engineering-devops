#!/usr/bin/python3
""" This module using this REST API,
for a given employee ID, returns information
about his/her TODO list progress. """

import csv
import requests
import sys


if __name__ == "__main__":

    query1 = {"id": sys.argv[1]}
    query = {"userId": sys.argv[1]}

    with requests.get(
            "https://jsonplaceholder.typicode.com/users",
            params=query1
            ) as result1:
        pass
    with requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params=query
            ) as result:
        ls = result.json()
        name = result1.json()[0].get("username")
        f_name = "{}.csv".format(sys.argv[1])

        with open(f_name, "w", newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [sys.argv[1], name, t.get("completed"), t.get("title")]
                ) for t in ls]
