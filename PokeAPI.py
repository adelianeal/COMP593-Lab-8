import requests
def get_poke_info(pokemon):
    """ Gets all information about a specified Pokemonretrieved from the PokeAPI

    :param name: Pokemon name
    :returns: Dictionary of Pokemon info, if successful. None, if not. 
    """

    resp_msg = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon)

    if resp_msg.status_code == 200:
        return resp_msg.json()   
    else:
        return