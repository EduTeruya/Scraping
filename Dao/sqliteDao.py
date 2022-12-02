import sqlite3

class SqliteDao:
 
    def __init__(self): 
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()

    def saveData(self, table, source, data, key, value):
        for ind in data.index:
            self.cursor.execute("INSERT INTO "+table+"(SOURCE, MODEL, PRICE) VALUES('"+source+"', '"+data[key][ind]+"','"+data[value][ind]+"')")
        self.conn.commit()
        
    def close(self):
        self.conn.close()
        

