import psycopg2
from psycopg2 import Error
from codecs import open
from pathlib import *
from typing import Union


class DBAccess():
    def __init__(self) -> None:
        """
        Class to initialise the Database Class. Initialisation function
        connects to DB, gets version and checks connection status
        """
        try:
            # Connect to database
            self.connection = psycopg2.connect(user="postgres",
                                               password="postgres",
                                               host="db",
                                               port="5432",
                                               database="postgres")

            # Create a cursor to perform database operations
            self.cursor = self.connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(self.connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            self.cursor.execute("SELECT version();")
            # Fetch result
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_sql_on_postgres(self, sql_command: str) -> Union[list, print]:
        """
        Function to execute SQL Script on Table
        :param sql_command: SQL command, string
        :return: Returns records if Select statement is executed, otherwise just returns success or failure message
        """
        try:
            self.cursor.execute(sql_command)
            self.connection.commit()
            if self.cursor.description is not None:
                records = self.cursor.fetchall()
                print(f"Query written to SQL Table - {sql_command}")
                return records
            return print(f"Query written to SQL Table - {sql_command}")
        except (Exception, Error) as error:
            print("Error Writing to DB")
            raise error


    def read_sql(self, sql_file_path: str) -> str:
        """
        Function to Read SQL file from Repo
        :param sql_file_path: SQL File Path, string
        :return: Returns SQL Script, string
        """
        try:
            with open(sql_file_path, 'r') as s:
                sql_script = s.read()
                return sql_script
        except (Exception, Error) as error:
            print("Error Reading SQL File")
            raise error

    def create_table(self) -> None:
        """
        Function to read file path and create SQL tables
        :return: None
        """
        file_path = Path.cwd() / 'src' / 'helpers' / 'create_tables.sql'
        self.execute_sql_on_postgres(self.read_sql(str(file_path)))

    def close_db_connection(self) -> None:
        """
        Function to close database connection
        :return:
        """
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

