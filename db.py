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
        sql = ''' INSERT INTO musicalinstruments (name)
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
        sql = ''' INSERT INTO notes(note, frequency,musicalinstrument_id)
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
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql2 = """CREATE TABLE IF NOT EXISTS notes (
                                    id integer PRIMARY KEY,
                                    note text NOT NULL,
                                    musicalinstrument_id integer NOT NULL,
                                    frequency integer NOT NULL,
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
        if conn:
            conn.close()
    else:
        print("error crete table")

