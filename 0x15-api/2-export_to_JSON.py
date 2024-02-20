#!/usr/bin/python3
""" This module using this REST API,
for a given employee ID, returns information
about his/her TODO list progress. """

import csv
import json
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
        f_name = "{}.json".format(sys.argv[1])

        dic = {sys.argv[1]: ls}
        for i in dic.get(sys.argv[1]):
            del i["userId"]
            del i["id"]
            i["username"] = name

        with open(f_name, "w") as file:
            json.dump(dic, file)
