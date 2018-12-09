from palette_import_lib import *
import os

my_dir = os.path.dirname(os.path.realpath(__file__))

palette_filename = 'CHROMA.MAP.csv'

palette_dict = read_palette_from_file(my_dir + '/' + palette_filename)



#print(palette_dict)
print('results of the dictionary read')
print(f'{palette_dict[0]}')
print(f'{palette_dict[1]}')
print(f'{palette_dict[2]}')
