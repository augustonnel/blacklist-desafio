from flask import request, Response
from database import Database
import sqlite3

def get_whitelist():
    # Create an instance of database
    database = Database()

    # Mount query to fetch all whitelist from database
    query = """
    SELECT * FROM whitelist;
    """

    # Call function that should execute query
    whitelist = database.execute_select_query(query)

    return whitelist

def add_to_whitelist():
    # Check if request has correct body (with ip address in JSON format)
    if request.data and request.json['ip']:
        try:
            # Create an instance of database
            database = Database()

            # Mount query to insert data to database
            query = """
            INSERT INTO whitelist (ip)
            VALUES (?)
            """

            # Call function that should execute query
            database.execute_insert_query(query, [(request.json['ip'], )])
            
            return {
                'message': 'This IP address was inserted successfuly'
            }, 201
        except sqlite3.IntegrityError:
            # Return error when ip already exists on database
            return {
                'error': 'IP already exists in whitelist'
            }, 409
        except Exception:
            # Return unkown error
            return {
                'error': 'Something went wrong, please try again.'
            }, 500
    else:
        # Return error when ip was not found on body request
        return { 'error': 'Please, send a valid ip' }, 400