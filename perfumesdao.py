# Python Database Access Object
# This programe perfoms CRUD operation on MySQL datase
# using python to control database

import mysql.connector
import dbconfig as cfg

# Define an Object class
class perfumeDAO:

    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    # Initialize the class
    def __init__(self):
        # reading from config file
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.table = cfg.mysql['table']
        self.connection = None
        self.cursor = None
    
    # Function to define the cursor to interact with the database
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Function to create a new record in the database
    def create(self, data):
        cursor = self.getCursor()
        sql =  f"insert into {self.table} (Name,Brand,Size_ml,Price_eur,Gender) values (%s,%s,%s,%s,%s)"
        values = [
            data["Name"],
            data["Brand"],
            data["Size_ml"],
            data["Price_eur"],
            data["Gender"]
        ]
        cursor.execute(sql,values)
        
        self.connection.commit()
        self.closeAll
        return cursor.lastrowid
              
    # Function to get all records from the database rows
    def getAll(self):
        cursor = self.getCursor()
        sql = f"select * from {self.table}"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)
        self.closeAll()
        return returnArray

    # Function to find a specific record by id
    def findById(self,id):
        cursor = self.getCursor()
        sql = f"select * from {self.table} where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)

    # Function to update existing record
    def update(self,data):
        cursor= self.getCursor()
        sql = f"update {self.table} set Name = %s, Brand = %s, Size_ml = %s, Price_eur = %s, Gender = %s where id = %s;"
        values = [          
            data["Name"],
            data["Brand"],
            data["Size_ml"],
            data["Price_eur"],
            data["Gender"],
            data["id"]          
        ]
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return data

    # Function to delete a record
    def delete(self,id):
        cursor = self.getCursor()
        sql = f"delete from {self.table} where id = %s"
        values = (id,)

        cursor.execute(sql,values)

        self.connection.commit()
        print("Deletion complete")
        self.closeAll
        return {}

    # Function to convert a record to a dict object
    def convertToDict(self,result):
        colnames = ["id","Name","Brand","Size_ml","Price_eur","Gender"]

        perfume = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                perfume[colName]= value
            return perfume

  
# creates a new class
perfumeDAO = perfumeDAO()    

if __name__== "__main__":

    print("The Perfume Shop")