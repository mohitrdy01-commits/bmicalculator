from pymysql import connect 

def get_connection():
    connection = connect (
    host = "localhost",
    user = "root",
    password = "Mohit123098$",
    database= "bmicalculator"
    )
    return connection