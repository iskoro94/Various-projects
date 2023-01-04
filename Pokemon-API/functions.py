import requests
import json
from statistics import mode

def prepare_data_1():
  basic_names=['name', 'id', 'order', 'height', 'weight']
  stat_names=['hp', 'attack', 'defense', 'special_attack','special_defense', 'speed']
  #create empty dictionary that holds the pokemon
  pokemon={}
  for i in range(1, 152):
    #get pokemon data from the API
    data=requests.get('https://pokeapi.co/api/v2/pokemon/'+str(i)).json()
    #save every pokemon as a dictionary in the form id : stat
    pokemon[i]={x: data[x] for x in basic_names}
    pokemon[i].update({x: data['stats'][j]['base_stat'] for j, x in enumerate(stat_names)})
  with open('data.json', 'w') as f:
    json.dump(pokemon, f)


def get_sum(stat):
  with open('data.json', 'r') as f:
    pokemon = json.load(f)
  return sum([pokemon[str(i)][stat] for i in range(1, 152)])


def get_mode(stat):
  with open('data.json', 'r') as f:
    pokemon = json.load(f)
  return mode([pokemon[str(i)][stat] for i in range(1, 152)])


def get_min(stat):
  with open('data.json', 'r') as f:
    pokemon = json.load(f)
  return min([pokemon[str(i)][stat] for i in range(1, 152)])


def prepare_data_2():
  basic_names = ['name', 'id', 'order', 'height', 'weight']
  stat_names = ['hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']
  pokemon = {}
  for i in range(1, 905):
    data = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i)).json()
    pokemon[i] = {x: data[x] for x in basic_names}
    pokemon[i].update({x: data['stats'][j]['base_stat'] for j, x in enumerate(stat_names)})
  types={}
  for i in range(1, 19):
    data=requests.get('https://pokeapi.co/api/v2/type/'+str(i)).json()
    #save every type as a dictionary in the form {type : list of pokemon ids of that type}
    types.update({data['name']: [data['pokemon'][j]['pokemon']['url'][34:-1] for j in range(len(data['pokemon']))]})
  moves={}
  for i in range(1, 826):
    data=requests.get('https://pokeapi.co/api/v2/move/'+str(i)).json()
    #save every move as a dictionary in the form {move : list of pokemon ids that can learn that move}
    moves.update({data['name']: [data['learned_by_pokemon'][j]['url'][34:-1] for j in range(len(data['learned_by_pokemon']))]})
  #save 'all', type and move that contains every pokemon
  types['all']=[str(pokemon[i]['order']) for i in range(1, 905)]
  moves['all']=types['all']
  with open('data2.json', 'w') as f:
    json.dump(pokemon, f)
  with open('types.json', 'w') as f:
    json.dump(types, f)
  with open('moves.json', 'w') as f:
    json.dump(moves, f)


def get_best(move, type1, stat):
  with open('types.json', 'r') as f:
    a = json.load(f)
  with open('moves.json', 'r') as f:
    b = json.load(f)
  with open('data2.json', 'r') as f:
    c = json.load(f)
  #find list of pokemon ids that have the given type and can learn the given move
  pok=list(set(a[type1]).intersection(b[move]))
  #get dictionary in the form {id: stat} for the given stat
  pok_data={str(i): c[str(i)][stat] for i in range(1,905)}
  #get pokemon data for the ids in pok
  pok_data={k: pok_data[k] for k in pok if k in pok_data}
  if pok_data == {}:
    return 'There is no such Pokemon'
  #get pokemon ids that have the maximum stat value
  max_pokemon=[k for k in pok_data if pok_data[k]==max(pok_data.values())]
  #return list of dictionaries of pokemon with the maximum stat value
  return [{c[i]['name']: c[i][stat]} for i in max_pokemon]