import requests
import json
from src.helpers.postgres_access import DBAccess


class Pokemon:

    def __init__(self):
        """
        Class to execute pokemon queries. Init function prepares base URL
        :return Returns base URL for API Call
        """
        self.url = "https://pokeapi.co/api/v2/pokemon?limit="
        print("Pokemon Class Initialised")

    def get_data_pokemon_api(self, qty: int = 5) -> str:
        """
        Function to call Pokemon API and get response
        :param qty: Quantity of pokemon to call, int, default 5
        :return: JSON response from the server
        """
        try:
            self.url = self.url + str(qty)
            response = requests.get(self.url).text
            self.response_json = json.loads(response)
            return self.response_json
        except Exception as error:
            raise error

    def construct_sql(self, table_name: str, action: str) -> list:
        """
        Function to construct SQL query
        :param table_name: Name of table, str
        :param action: Desired Action - Insert or Update, str
        :return: List of insert SQL Statements
        """
        self.sql_list = []
        if action == "insert":
            for items in self.response_json["results"]:
                sql_statement_insert = f"""\
                insert into {table_name} (pokemon_id, pokemon_name, pokemon_url) values ({items['url'].split('/')[-2:][0]},'{items['name']}', '{items['url']}') ON CONFLICT (pokemon_id) DO NOTHING; """
                self.sql_list.append(sql_statement_insert.strip())
        # elif action == "update":
        #     for items in response_json["results"]:
        #         sql_statement_insert = f"""\
        #         update {table_name} set pokemon_id = {items['url'][-2:].strip("/")}, pokemon_name='{items['name']}', pokemon_url='{items['url']}';
        #         """
        #         sql_list.append(sql_statement_insert.strip())
        return self.sql_list

    def store_pokemon(self) -> None:
        """
        Function to store pokemon data in database
        :return: None
        """
        try:
            db_obj = DBAccess()
            self.sql_list = self.construct_sql("pokemon", action="insert")
            for items in self.sql_list:
                db_obj.execute_sql_on_postgres(items)
            db_obj.close_db_connection()
        except Exception as error:
            raise error

    def get_pokemon(self):
        """
        Function to get all pokemon data from DB
        :return: Records, list
        """
        try:
            db_obj = DBAccess()
            get_sql = "select * from pokemon"
            records = db_obj.execute_sql_on_postgres(get_sql)
            return records
        except Exception as error:
            raise error
