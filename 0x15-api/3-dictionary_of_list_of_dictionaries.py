#!/usr/bin/python3
""" This module using this REST API,
for a given employee ID, returns information
about his/her TODO list progress. """

import csv
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    f_url = "{}users".format(url)
    d_url = "{}todos".format(url)
    users = requests.get(f_url).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(d_url,
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
