""" Returns error message whenone does not input characters within the range of 1-50"""
import requests

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



def main():

    print("Getting some data from'jsonplaceholder.typicode.com' website")

    url = "https://jsonplaceholder.typicode.com/posts/"

    post_id = input("Enter a No between 1 and 50: ")

    print("Getting your request...")

    get_r = get_data(url,post_id)

    print("GET Response data Status code Headers" % ("-"*13,get_r.text, "-"*21, get_r.status_code,"-"*2, get_r.headers))



if __name__ == '__main__':

    main()
