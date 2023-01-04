from functions import *
import time

start = time.perf_counter()
prepare_data_1()
end = time.perf_counter()
print(f'Running time for prepare_data_1: {end-start}')

start = time.perf_counter()
prepare_data_2()
end = time.perf_counter()
print(f'Running time for prepare_data_2: {end-start}')

start = time.perf_counter()
get_sum('defense')
end = time.perf_counter()
print(f'Running time for get_sum: {end-start}')

start = time.perf_counter()
get_mode('defense')
end = time.perf_counter()
print(f'Running time for get_mode: {end-start}')

start = time.perf_counter()
get_min('defense')
end = time.perf_counter()
print(f'Running time for get_min: {end-start}')

start = time.perf_counter()
get_best('all', 'all', 'hp')
end = time.perf_counter()
print(f'Running time for get_best: {end-start}')

print('The best pokemon for cut, rock, attack are: {}'.format(get_best('cut', 'rock', 'attack')))
print('The best pokemon for all, ice, speed are: {}'.format(get_best('all', 'ice', 'speed')))
print('The best pokemon for laser-focus, all, hp are: {}'.format(get_best('laser-focus', 'all', 'hp')))
print('The best pokemon for light-screen, rock, special_attack are: {}'.format(get_best('light-screen', 'rock', 'special_attack')))
print('The best pokemon for mega-kick, water, special_defense are: {}'.format(get_best('mega-kick', 'water', 'special_defense')))
