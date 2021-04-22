from pymongo import MongoClient
class Dbconn():
    def __init__(self):
        try:
            self.client = MongoClient('localhost', 27017)
            print("DB connected successfully")
        except:
            print("Could not connect to MONGODB")
        self.mydb = self.client['sitechecker']
        self.mycollection = self.mydb['httpstatuscodes']

    def query(self, httpcode):
        status_code = (str(httpcode))
        cursor = self.mycollection.find()
        for record in cursor:
            if record['title'][0] == status_code[0]:
                print(record['codes'][status_code])