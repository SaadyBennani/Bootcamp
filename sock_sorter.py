# sock_sorter.py

import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_list = []
sock_counter = {}
sock_colors = ['black', 'white', 'blue']

# generates a list of 100 socks mixed with types and colors

for i in range(100):
    sock = random.choice(sock_types)
    color = random.choice(sock_colors)
    sock_list.append((color, sock))
    # sock counter
    sock_counter[(color, sock)] = sock_counter.get((color, sock), 0) + 1

print(sock_list)
print(sock_counter)

for sock in sock_counter:
    print(f'{sock} has {sock_counter[sock]%2} loner(s)')
