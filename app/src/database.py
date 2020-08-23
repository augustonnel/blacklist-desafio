import sqlite3
import logging
logging.root.setLevel(logging.INFO)

class Database:
    def __init__(self):
        self.conn = None

    def create_connection(self):
        # Create connection with database
        logging.info('########## Connecting to database')
        self.conn = sqlite3.connect('torblacklist.db')
    
    def close_connection(self):
        # Close connection with database
        logging.info('########## Desconnecting from database')
        self.conn.close()

    def create_database(self):
        # Create database structure (tables)
        try:
            logging.info('########## Criando tabela...')
            self.create_connection()
            cursor = self.conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS whitelist (
                    ip TEXT NOT NULL PRIMARY KEY
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS blacklist (
                    ip TEXT NOT NULL PRIMARY KEY
            );
            """)

            logging.info('########## Tabela criada com sucesso!')
        except Exception:
            logging.exception('########## Error creating database')
        finally:
            self.close_connection()

    def execute_insert_query(self, query, values):
        try:
            logging.info('########## Executing query {} with values {}'.format(query, values))
            self.create_connection()
            cursor = self.conn.cursor()
            cursor.executemany(query, values)

            self.conn.commit()
        except sqlite3.IntegrityError:
            logging.exception('########## Error inserting data. Register already exists.')
            raise
        except Exception:
            logging.exception('########## Error inserting data. Something went wrong.')
            raise
        finally:
            self.close_connection()

    def execute_select_query(self, query):
        try:
            logging.info('########## Executing query {}'.format(query))

            self.create_connection()
            cursor = self.conn.cursor()
            cursor.execute(query)

            return cursor.fetchall()
        except Exception:
            logging.exception('########## Error fetching data')
        finally:
            self.close_connection()
