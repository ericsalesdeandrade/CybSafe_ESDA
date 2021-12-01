from src.get_pokemon import Pokemon

poke_obj = Pokemon()


# Unit test to check whether correct Pokemon URL is initialised
def test_pokemon_url():
    assert poke_obj.url == "https://pokeapi.co/api/v2/pokemon?limit=", "failed"


# Unit test to check whether correct SQL statement is generated
def test_construct_sql():
    table_name = "pokemon"
    action = "insert"
    poke_obj.response_json = poke_obj.get_data_pokemon_api()
    poke_obj.response_json["results"] = [{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
                                         {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'},
                                         {'name': 'venusaur', 'url': 'https://pokeapi.co/api/v2/pokemon/3/'},
                                         {'name': 'charmander', 'url': 'https://pokeapi.co/api/v2/pokemon/4/'},
                                         {'name': 'charmeleon', 'url': 'https://pokeapi.co/api/v2/pokemon/5/'}]
    sql_list = poke_obj.construct_sql(table_name, action)
    assert sql_list[0] == "insert into pokemon (pokemon_id, pokemon_name, pokemon_url) values (1,'bulbasaur', " \
                          "'https://pokeapi.co/api/v2/pokemon/1/') ON CONFLICT (pokemon_id) DO NOTHING;", "failed "
