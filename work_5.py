#                        Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#        Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.





with open('my_file.txt', 'w') as data:
    data.write('1\n')
    data.write('2\n')
    data.write('3\n')
    data.write('4\n')

n = int(input('Введите число: '))
my_list = []
for i in range(-n, n + 1):
    my_list.append(i)   
print(my_list)

count = 1
with open('my_file.txt', 'r') as data:
    for j in data:
        count *= my_list[int(j)]
print(count)
