#!/usr/bin/python3
""" This model queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0."""

import requests


def top_ten(subreddit):
    """ This model queries the Reddit API and returns thenumbe
    0of subscribers (not active users, total subscribers)for a
    given subreddit. If an invalid subreddit is given,
    the function should return 0."""

    headers = {'User-Agent': "Firefox/123.0"}
    url = "https://www.`reddit.com/r/{}/about.json".format(subreddit)
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(cil.get("data").get("title")) for cil in results.get("children")]
