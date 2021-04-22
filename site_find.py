from pymongo import MongoClient
import requests
import db_conn
url = "http://the-internet.herokuapp.com/status_codes/305"

def GetHTTPstatus(url1):
    status = requests.get(url1).status_code
    return status
dbconnect = db_conn.Dbconn()
dbconnect.query(GetHTTPstatus(url))