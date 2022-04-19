from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        #Init to connect to mongodb without authentication
        #self.client = MongoClient('mongodb://localhost:54815')
        #init connect to mongodb with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:54815/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty.")

# Create method to implement the R in CRUD.
    def read_all(self, data):
            cursor = self.database.animals.find(data, {'_id':False})#returns a cursor which points to a list in AAC database
            return cursor
        
    def read(self,data):
            return self.database.animals.find_one(data) #returns one document as python dictionary
        
#Method to implement the U in CRUD
    def update(self, query, data):
        if data is not None:
            self.database.animals.update_one(query, data) #Updates document from AAC database
            

#Method to implement the D In CRUD
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_many(data) #Deletes document from AAC database
            
            
        
            