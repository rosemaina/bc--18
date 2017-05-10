""" Returns error message when one does not input numbers within the range from 1-50"""
import urllib.request

import urllib.parse

# url = '<a href="https://api.spotify.com/v1/search?type=artist&q=snoop">https://api.spotify.com/v1/search?type=artist&q=snoop</a>'

# f = urllib.request.urlopen(url)

# print(f.read().decode('utf-8'))

def get_data(get_url, post_id):


    try:

        isinstance(int(post_id), int)

        if int(post_id) <= 50 and int(post_id) > 0:

            r = urllib.request.urlopen(get_url + post_id)

            return r.read().decode('utf-8')

        else:

            print("Enter a No between 1 and 50")

    except ValueError as e:

        print("A whole number is required for your request to succeed")

        raise(e)

    return "* 404 *"


def main():

    print("Getting some data from'jsonplaceholder.typicode.com' website")

    url = "https://jsonplaceholder.typicode.com/posts/"

    post_id = input("Enter a number between 1 and 50:")

    print("Getting the request...")

    get_r = get_data(url, post_id)


    print("GET Response data Status code Headers" % ("-"*13,get_r.text, "-"*21, get_r.status_code,"-"*2, get_r.headers))


