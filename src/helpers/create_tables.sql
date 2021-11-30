--Create UID Extention
CREATE EXTENSION if not exists "uuid-ossp";

--Create table Pokemon with primary and unique id from API URL
CREATE TABLE if not exists pokemon (
	pokemon_key uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	pokemon_id integer UNIQUE,
	pokemon_name varchar (255),
	pokemon_url varchar (255)
);