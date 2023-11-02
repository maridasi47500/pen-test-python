import sqlite3
from sqlite3 import Error

class Db():
  db=r"./pythonsqlite.db"
  def get_db():
      return self.db
  def create_connection(self,db_file):
      """ create a database connection to a SQLite database """
      conn = None
      try:
          conn = sqlite3.connect(db_file)
          print(sqlite3.version)
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()
  def create_table(self,conn, create_table_sql):
      """ create a table from the create_table_sql statement
      :param conn: Connection object
      :param create_table_sql: a CREATE TABLE statement
      :return:
      """
      try:
          c = conn.cursor()
          c.execute(create_table_sql)
      except Error as e:
          print(e)
  def get_notes_instrument(self,name):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select musicalinstruments.name, notes.frequency, notes.note from musicalinstruments left join notes on notes.musicalinstrument_id = musicalinstruments.id where name = ?'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql,(name,))
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def get_notes(self,name,note):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select musicalinstruments.name, notes.frequency, notes.note from musicalinstruments left join notes on notes.musicalinstrument_id = musicalinstruments.id where note = ? and name = ?'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql,(note, name))
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def get_othermusicalinstruments(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from musicalinstruments '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def get_musicalinstruments(self):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select musicalinstruments.name, notes.frequency, notes.note from musicalinstruments left join notes on notes.musicalinstrument_id = musicalinstruments.id '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def create_musicali(self,conn, project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' INSERT OR IGNORE INTO musicalinstruments (name)
                  VALUES(?) '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        print(cur.lastrowid)
        return cur.lastrowid
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def create_tuner(self,conn, project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' INSERT OR IGNORE INTO notes(note, frequency,musicalinstrument_id)
                  VALUES(?,?,?) '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid
      except Error as e:
        print(e)
        return []
      finally:
          if conn:
              conn.close()
  def __init__(self):


    sql1 = """ CREATE TABLE IF NOT EXISTS musicalinstruments (
                                        id integer PRIMARY KEY autoincrement,
                                        name text NOT NULL unique
                                    ); """

    sql2 = """CREATE TABLE IF NOT EXISTS notes (
                                    id integer PRIMARY KEY autoincrement,
                                    note text NOT NULL,
                                    musicalinstrument_id integer NOT NULL,
                                    frequency float NOT NULL,
                                        UNIQUE(musicalinstrument_id, note) ON CONFLICT REPLACE,
                                    FOREIGN KEY (musicalinstrument_id) REFERENCES musicalinstruments (id)
                                );"""
    self.create_connection(self.db)
    conn = sqlite3.connect(self.db)
    if conn is not None:
        self.create_table(conn,sql1)
        self.create_table(conn,sql2)
        print("key")
        myarr=("violon",)
        self.create_musicali(conn,myarr)
        print("key")
        myarr=("la", 440, 1,)
        self.create_tuner(conn,myarr)
        myarr=("mi", 659.25, 1,)
        self.create_tuner(conn,myarr)
        myarr=("re", 293.66, 1,)
        self.create_tuner(conn,myarr)
        myarr=("sol", 196.00, 1,)
        self.create_tuner(conn,myarr)
        if conn:
            conn.close()
    else:
        print("error crete table")

