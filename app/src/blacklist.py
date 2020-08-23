# used to get params (status, response, etc) from own request (example: call from our api /blacklists)
from flask import request
from database import Database
from whitelist import get_whitelist
import logging
logging.root.setLevel(logging.INFO)

# used to make http requests from another apis (example: torlist)
import requests

def get_blacklist_from_source():
    # request to torlist
    response = requests.get('https://www.dan.me.uk/torlist/')

    #checking status response
    if response.status_code == 403:
        return {
            "error": 'You have already requested this api in the last 30 minutes'
        }, 403
    elif response.status_code == 200:
        blacklist_array = response.text.split()

        json_response = {
            "blacklist": blacklist_array
        }
        return json_response
    else:
        # generic error
        return {
            "error": 'Something went wrong'
        }, 500

# function that was called by /blacklist route (in server.py line 9)
def get_blacklist():
    # request to torlist
    response = requests.get('https://www.dan.me.uk/torlist/')

    database = Database()
    
    #checking status response
    if response.status_code == 200 or response.status_code == 403:
        blacklist_array = []
        whitelist_array = get_whitelist()

        if response.status_code == 200:
            blacklist_array = response.text.split()
            blacklist_array_tuples = []

            for item in blacklist_array:
                blacklist_array_tuples.append((item,))

            query = """
            INSERT INTO blacklist (ip)
            VALUES (?)
            """

            database.execute_insert_query(query, blacklist_array_tuples)
        else:
            # Mount query to fetch all whitelist from database
            query = """
            SELECT * FROM blacklist;
            """

            blacklist_array_tuples = database.execute_select_query(query)
            for ip in blacklist_array_tuples:
                blacklist_array.append(ip[0])

        # removing whitelist ip`s from blacklist
        for ip in whitelist_array:
            if ip[0] in blacklist_array:
                blacklist_array.remove(ip[0])

        return {
            "blacklist": blacklist_array
        }
    else:
        # generic error
        return {
            "error": 'Something went wrong'
        }, 500