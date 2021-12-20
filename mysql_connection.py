import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yhdbshin.cjdnoifmay48.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '0000'
    )
    return connection

    