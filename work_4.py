#                      Реализуйте алгоритм перемешивания списка.

import random
 
my_list = []
n = 10
for i in range(n):
    my_list.append(random.randint(1, 9))
print(f'Список до перемешивания:\n{my_list}')
random.shuffle(my_list)
print(f'Список после перемешивания:\n{my_list}')