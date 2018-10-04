"""
Module For Setting Up Database
"""
import os
import psycopg2

class DBAccess(object):
    """
    Class Contains Method For Creating
    And Connecting To Database
    """
    @staticmethod
    def db_connection():
        """
        Method For Establishing Connection To Databse
        """
        connection = psycopg2.connect(
            "dbname='d4or467mumdvnf' user='bzjrdbxajezifp' host='ec2-23-23-80-20.compute-1.amazonaws.com' password='004afaa0dfedda5ec4bfb867d47e98a7417b6913c16f91c8019b60cf67bb168c' port='5432'"
        )
        return connection     

    @staticmethod
    def create_databasetables():
        """
        Method For Creating Tables In Database.
        """
        table_creation_query = (
            """
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email_address VARCHAR(50) UNIQUE NOT NULL,
                    phone_number VARCHAR(11) NOT NULL,
                    password VARCHAR(250) NOT NULL,
                    is_loggedin BOOLEAN DEFAULT FALSE
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "admin" (
                    admin_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email_address VARCHAR(50) UNIQUE NOT NULL,
                    phone_number VARCHAR(11) NOT NULL,
                    password VARCHAR(250) NOT NULL,
                    is_loggedin BOOLEAN DEFAULT FALSE
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "menu" (
                    item_id SERIAL PRIMARY KEY,
                    admin_id INTEGER NOT NULL,
                    item_category VARCHAR(30) NOT NULL,
                    item_name VARCHAR(30) NOT NULL,
                    price INTEGER NOT NULL,
                    FOREIGN KEY (admin_id)
                    REFERENCES "admin" (admin_id)
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "order" (
                    order_id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    totalamount INTEGER NOT NULL,
                    payment_mode VARCHAR(30) NOT NULL,
                    order_status VARCHAR(30) NOT NULL,
                    FOREIGN KEY (user_id)
                    REFERENCES "users" (user_id)
                )
            """,)
           
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            for query in table_creation_query:
                cur.execute(query)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
