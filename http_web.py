
""" Returns error message whenone does not input characters within the range of 1-50"""

import json

def get_data(get_url, post_id):
    

    try:
        isinstance(int(post_id), int)
        if int(post_id) <= 50 and int(post_id) > 0:
            r = requests.get(get_url + post_id)
            return r
        else:
            print("Enter a No between 1 and 50")
    except ValueError as e:

        print("A whole number is required for your request to succeed")
        raise(e)
    return "* Error Message*"
