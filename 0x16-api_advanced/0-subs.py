#!/usr/bin/python3
""" This model queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """ This model queries the Reddit API and returns thenumbe
    0of subscribers (not active users, total subscribers)for a
    given subreddit. If an invalid subreddit is given,
    the function should return 0."""

    headers = {'User-Agent': "Firefox/123.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()["data"].get("subscribers")
    return 0
