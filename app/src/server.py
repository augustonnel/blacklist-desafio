from flask import Flask
from flask import request
from blacklist import get_blacklist, get_blacklist_from_source
from whitelist import get_whitelist, add_to_whitelist
from database import Database

app = Flask(__name__)

@app.route('/blacklist-proxy', methods=['GET'])
def blacklist_proxy():
    return get_blacklist_from_source()

@app.route('/blacklist', methods=['GET'])
def blacklist():
    return get_blacklist()

@app.route('/whitelist', methods=['POST'])
def whitelist():
    return add_to_whitelist()

if __name__ == "__main__":
   Database().create_database()
   app.run(host='0.0.0.0')
