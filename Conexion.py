# -*- coding: utf-8 -*-
import mysql.connector


class Conexion(object):
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="root", database="python")
        self.cursor = self.db.cursor()

    def executeNonQuery(self, sql):
        print("EJECUTO: %s" % sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except mysql.connector.Error as e:
            self.db.rollback()
            print("MySQL Error: %s" % str(e))
            return False

    def executeQuery(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print("MySQL Error: %s" % str(e))
            self.db.close()
            return None

    def executeOneQuery(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except:
            return None

    def close(self):
        self.db.close()
