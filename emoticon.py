#emoticon.py
list_eyes = [';',':','8','B','=']
list_noses = [' ', '','o']
list_mouths = ['o', 'O', 'p', 'P','|', 'C']

import random

out_string = ''

#random eyes

out_string = out_string + random.choice(list_eyes)

# random noses_list

out_string = out_string + random.choice(list_noses)

# random mouths

out_string = out_string + random.choice(list_mouths)

print(out_string)
