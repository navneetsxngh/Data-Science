import mysql.connector

class UserModel():
    def __init__(self):
        # Connection Establishment
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Lenovoloq@123",
                    database="flask_db")
            print("Connection Successful")
        except Exception as e:
            print(str(e))

    def user_getall_model(self):
        
        ## Query Execution
        return "This is User Sign up Model"