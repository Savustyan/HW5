s = '''Шесты начали одеваться цветными полотнищами. Один павильон особенно отличался размерами: в него поместилось даже 
большое старое дерево, росшее посреди луга. Теперь ветки его украсились множеством фонариков, пришедшихся как раз над 
главным столом. Красиво, конечно, но хоббитов больше занимала кухня, сооруженная прямо под открытым небом в северном 
углу луга. Там с утра до ночи суетилось множество поваров и поварят из окрестных трактиров, призванных в помощь гномам и
 прочему пришлому люду, поселившемуся в последнее время на Горке. Возбуждение, владевшее хоббитами, достигло предела.'''

print('Longest word:')
print(max(s.split(), key=len))

import string
s = str.lower(s)
frequency = {}

for word in s.split():
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

def get_key(d, value):
    for k, v in frequency.items():
        if v == value:
            return k
print('Meet most times:')
print(get_key(frequency, max(frequency.values())), max(frequency.values()), 'times')

