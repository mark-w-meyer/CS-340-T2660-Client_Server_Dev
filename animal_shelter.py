from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:53141/AAC' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:53141')
            
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data, option):
      
        if data is not None:
            if option is "one":
                creation = self.database.animals.insert_one(data)  # data should be dictionary 
                return True
            elif option is "many":
                creation = self.database.animals.insert_many(data) # data should be dicitonary
                return True
        else:
            raise Exception("Nothing to save because data parameter is empty")
            return False           
            
    # Create method to implement the R in CRUD.
    def read(self,searchCriteria, option):

        # if criteria is not None then this find will return one row which matches the criteria
        if searchCriteria is not None:
            if option is "one":
                searchData = self.database.animals.find_one(searchCriteria,{"_id":False})
            elif option is "many":
                searchData = self.database.animals.find(searchCriteria,{"_id":False})
                
            if searchData:
                print("Read successful")
            else:
                print("Read failed")
        else:            
            raise Exception("Nothing to search because search parameter is empty")
            
        return searchData
    
    # Create method to implement the U in CRUD
    def update(self, filter, data, option):
        
        # use dictionary to identify entry to be updated
        filter_data = filter
        
        # use dictionary to update data component within filter_data
        new_data = { "$set": data }
        
        # if data is not None then update the database with new data within filtered data
        if data is not None:
            if option is "one":
                self.database.animals.update_one(filter_data, new_data) # data should be dictionary
                return True
            elif option is "many":       
                self.database.animals.update_many(filter_data, new_data) # data should be dictionary
                return True
        else:
            raise Exception("Nothing to update because parameter is empty")
            return False
        
    # Create method to implement the D in CRUD
    def delete(self, data, option):
    
        #if data is not None then delete the data from database
        if data is not None:
            if option is "one":               
                self.database.animals.delete_one(data) # data should be dictionary
                return True
            elif option is "many":
                self.database.animals.delete_many(data) # data should be dictionary
                return True
        else:
            raise Exception("Nothing to remove because parameter is empty")
            return False
    
