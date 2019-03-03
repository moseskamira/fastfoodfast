"""
Module Responsible For Each Transaction
In Database.
"""

import psycopg2
from db_connection import DBAccess


class DbTransaction(object):
    """
    Class Responsible For Different
    Database Transactions
    """

    @staticmethod
    def save(sql, data):
        """
        Method For Inserting Data Into Database Table
        """
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def fetch_one(sql, data):
        """
        Method For Retrieving Single Row From Database Table
        """
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            cur.execute(sql, data)
            row = cur.fetchone()
            cur.close()

            if row and not "":
                return row
            return None

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def fetch_all(sql, data=None):
        """
        Method Returns All Rows From Database Table
        """
        list_tuple = []
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            if data is not None:
                cur.execute(sql)
            else:
                cur.execute(sql, data)
            rows = cur.fetchall()
            for row in rows:
                list_tuple.append(row)
            cur.close()
            return list_tuple
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    
    @staticmethod
    def fetch_order_history(sql, data):
        """
        Method Returns All Rows From Database Table
        """
        list_tuple = []
        conn = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            if data == None:
                cur.execute(sql)
            else:
                cur.execute(sql, (data,))
            rows = cur.fetchall()
            for row in rows:
                list_tuple.append(row)
            cur.close()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def edit(sql, data):
        """
        Method For Editing Data In Database Table.
        """
        conn = None
        updated_rows = None
        try:
            conn = DBAccess.db_connection()
            cur = conn.cursor()
            cur.execute(sql, data)
            updated_rows = cur.rowcount
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(str(error))
        finally:
            if conn is not None:
                conn.close()
        return updated_rows
                