import random, sys, stdio
total = 0.0
count = 0
while not stdio.isEmpty():
    value = stdio.readFloat()
    total += value
    count += 1
print('Average is %f' %(total / count))


import random, sys, stdio
n = int(sys.argv[1])
for i in range(n):
    print(random.random())













import sys, random, stddraw
from color import DARK_GREEN, GRAY
n = int(sys.argv[1])
x,y = 0, 0
for i in range(n):
    cx = x
    cy = y
    c = random.uniform(0, 1)
    if c < 0.02:
        x = 0.50
        y = 0.27 * cy
    if 0.02 <= c < 0.17 :
        x = (-0.14 * cx) + (0.26 * cy) + 0.57
        y = (0.25 * cx) + (0.22 * cy) - 0.04
    if 0.17 <= c < 0.3:
        x = (0.17 * cx) - (0.21 * cy) + 0.41
        y = (0.22 * cx) + (0.18 * cy) + 0.09
    if 0.3 <= c <= 1.0:
        x = (0.78 * cx) + (0.03 * cy) + 0.11
        y = (-0.03 * cx) + (0.74 * cy) + 0.27
    stddraw.setPenRadius(0.0015)
    stddraw.setPenColor(DARK_GREEN)
    stddraw.point(x, y)
    stddraw.show(0)
stddraw.show()








x,y = 0, 0
for i in range(n):
    cx = x
    cy = y
    c = random.uniform(0, 1)
    if 0.0 <= c < 0.4 :
        x = 0.31 * cx - 0.53 * cy + 0.89
        y = -0.46 * cx - 0.29 * cy + 1.04
    if 0.4 <= c < 0.55:
        x = 0.31 * cx - 0.08 * cy + 0.22
        y = 0.15 * cx - 0.45 * cy + 0.34
    if 0.55 <= c <= 1.0:
        x = 0.55 * cy + 0.01
        y = 0.69 * cx - 0.20 * cy + 0.38
    stddraw.setPenRadius(0.0015)
    stddraw.setPenColor(GRAY)
    stddraw.point(x, y)
    stddraw.show(0)
stddraw.show()









import sys, stddraw, random
from color import GRAY
n = int(sys.argv[1])
stddraw.setXscale(-1.0, +1.0)
stddraw.setYscale(-1.0, +1.0)
RADIUS, dt = 0.05, 16.5
r = [0.0] * n
for i in range(n):
    r[i] = [random.random(), random.random()]
v = [0] * n
for i in range(n):
    v[i] = [random.uniform(0.015,0.025), random.uniform(0.015,0.025)]
dt *= n
while True:
    stddraw.clear(stddraw.GRAY)
    for i in range(n):
        stddraw.filledCircle(r[i][0], r[i][1], RADIUS)
        for j in range(n):
            if j == i: 
                if abs(r[j][0] + v[j][0]) + RADIUS > 1.0: v[j][0] = -v[j][0]
                if abs(r[j][1] + v[j][1]) + RADIUS > 1.0: v[j][1] = -v[j][1]
                r[j][0] += v[j][0]
                r[j][1] += v[j][1]
            else:
                if r[i][0] == r[j][0] and r[i][1] == r[j][1] : 
                    v[j][0] = +v[j][0]
                    v[j][1] = +v[j][1]
                    v[i][0] = -v[i][0]
                    v[i][1] = -v[i][1]
                if abs(r[j][0] + v[j][0]) + RADIUS > 1.0 : v[j][0] = -v[j][0]
                if abs(r[j][1] + v[j][1]) + RADIUS > 1.0 : v[j][1] = -v[j][1]
                r[j][0] += v[j][0]
                r[j][1] += v[j][1]
    stddraw.show(dt)
    

















"""

import sys, random
n = int(sys.argv[1])
trials = int(sys.argv[2])
dead_ends = 0
for t in range(trials):
    a = [[False] * n for i in range(n)]
    x, y = n // 2, n // 2
    while 0 < x < n - 1 and 0 < y < n - 1:
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            dead_ends += 1
            break
        a[x][y] = True
        r = random.random()
        if r < 0.25:
            if not a[x+1][y]: x += 1 
        elif r < 0.5:
            if not a[x-1][y]: x -= 1
        elif r < 0.75:
            if not a[x][y+1]: y += 1
        elif r < 1:
            if not a[x][y-1]: y -= 1
if (dead_ends // 100 != 0):
    print(str(dead_ends // 100) + '%' + ' dead end')
else:
    print('out')























Array_Matris = []
b = '\t'
x = int(input('تعداد سطر ها را وارد کنید : '))
y = int(input('تعداد ستون ها را وارد کنید : '))
for i in range(x):
    Array_Matris += [ [0] * y ]
for i in range(x):
    for j in range(y):
        Array_Matris[i][j] = input(f'[{i}][{j}] = ')
for i in  range(x):
    for j in range(y):
        if i == 0 :
            if j == 0:
                print(f"|''{b * (y - 1)}''|")
                print(f"| {Array_Matris[i][j]}", end='')
            elif j == (y - 1):
                print(f"\t{Array_Matris[i][j]} |")
            else:
                print(f'\t {Array_Matris[i][j]}', end='')
        elif i == (x - 1) :
            if j == 0:
                print(f"| {Array_Matris[i][j]}", end='')
            elif j == (y - 1):
                print(f"\t{Array_Matris[i][j]} |")
                print(f"|,,{b * (y - 1)},,|")
            else:
                print(f'\t {Array_Matris[i][j]}', end='')
        else:
            if j == 0:
                print(f"| {Array_Matris[i][j]}", end='')
            elif j == (y - 1):
                print(f"\t{Array_Matris[i][j]} |")
            else:
                print(f'\t {Array_Matris[i][j]}', end='')





Array_Matris = []
x = int(input('تعداد سطر ها را وارد کنید : '))
y = int(input('تعداد ستون ها را وارد کنید : '))
Array_Matris = [ [0] * y ] * x
for i in range(x):
    for j in range(y):
        Array_Matris[i][j] = input(f'[{i}][{j}] = ')
for i in range(x):
    for j in range(y):
        print(Array_Matris[i][j], end='\t')
    print()









b = '\t'
for i in  range(len(a)):
    for j in range(len(a[0])):
        if i == 0 :
            if j == 0:
                print(f"|''{b * (len(a[0]) - 1)}''|")
                print(f"| {a[i][j]}", end='')
            elif j == (len(a[0]) - 1):
                print(f"\t{a[i][j]} |")
            else:
                print(f'\t {a[i][j]}', end='')
        elif i == (len(a) - 1) :
            if j == 0:
                print(f"| {a[i][j]}", end='')
            elif j == (len(a[0]) - 1):
                print(f"\t{a[i][j]} |")
                print(f"|,,{b * (len(a[0]) - 1)},,|")
            else:
                print(f'\t {a[i][j]}', end='')


"""



























'''
Array_Matrix = []

x = int(input('تعداد سطر ها را وارد کنید : '))
y = int(input('تعداد ستون ها را وارد کنید : '))

for i in range(x):
    Array_Matrix += [ [0] * y ]

for i in range(x):
    for j in range(y):
        Array_Matrix[i][j] = input(f'[{i}][{j}] = ')
    print()

print(Array_Matrix)

for i in range(x):
    for j in range(y):

        print(Array_Matrix[i][j], end='\t')

    print()










import stddraw, random

n = 10000

cx = [0.0, 1.0, 0.500]
cy = [0.0, 0.0, 0.866]

x, y = 0, 0

for i in range(n):
    r = random.randrange(0, 3)
    x = (x + cx[r]) / 2.0
    y = (y + cy[r]) / 2.0
    stddraw.point(x, y)

stddraw.show()





Array_Matrix = []

x = int(input('تعداد سطر ها را وارد کنید : '))
y = int(input('تعداد ستون ها را وارد کنید : '))

for i in range(x):
    Array_Matrix += [ [0] * y ]

print(Array_Matrix)

for i in range(x):
    for j in range(y):
        Array_Matrix[i][j] = input(f'[{i}][{j}] = ')
    print()

Array_Matrix[0][0] = 999
print(Array_Matrix)


for i in range(x):
    for j in range(y):
        print(Array_Matrix[i][j], end=',\t')
    print()




import random

n = int(input("Number: "))

count = 0

Co_c = 0

IS_c = [False] * n

while Co_c < n :
    count +=1
    value = random.randrange(0,n)
    if not IS_c[value]:
        Co_c +=1
        IS_c[value] =True
print(IS_c)
print(count)

'''






























'''
Array_Matrix = []

x = int(input('تعداد سطر ها را وارد کنید : '))
y = int(input('تعداد ستون ها را وارد کنید : '))

Array_Matrix = [ [0] * y ] * x

print(Array_Matrix)

for i in range(x):
    for j in range(y):
        Array_Matrix[i][j] = input(f'[{i}][{j}] = ')
    print()

Array_Matrix[0][0] = 999
print(Array_Matrix)


for i in range(x):
    for j in range(y):
        print(Array_Matrix[i][j], end=',\t')
    print()

'''






























































"""

user = []
N_Student = int(input('تعداد دانش آموزان را وارد کنید: '))
for i in range(N_Student):
    DIR = {}
    Name_S = input(f'نام دانش آموز شماره {i + 1} :')
    Age_S = input(f'سن دانش اموز شماره {i + 1} :')
    Class_S = input(f'کلاس دانش اموز شماره {i + 1} : ')
    DIR = { Name_S:{
        'Age': Age_S,
        'Class': Class_S
    }}
    user.append(DIR)
for value in user:
    for name,item in value.items():
        print(f'''
#{name}: 
    Age:  {item.get("Age")}
    Class: {item.get('Class')}
---------------------------------------
''')





















SUITS = ['گشنیز', 'خشت', 'دل', 'اسپیک']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'سرباز', 'ملکه', 'شاه', 'تک']
deck = []
My_Card = {}
NomeCard = []
for S in SUITS:
    deck = []
    My_Card = {}
    for R in RANKS:
        card = R + '  ' + S
        deck += [card]
    My_Card[f'{S}'] = deck
    NomeCard.append(My_Card)
for i in NomeCard:
    print(f'{i} \n')








Number_St = int(input('تعداد دانشجویان را وارد کنید : '))
i = 1
if Number_St:
    while i <= Number_St:
        while True:
            Sr = float(input(f'نمره دانشجوی شماره {i} :'))
            if 20>=Sr>=0:
                break
            else:
                print('\n نمره مورد قبول نیست!!')
        if Sr < 10:
            print(f'\n دانشجوی شماره {i} مردود است!!')
        elif Sr >= 10:
            print(f'\n دانشجوی شماره {i} پاس است!!')
        i += 1

///////////////////////////////////////////////////////////

import random
ArrayMe = []
for i in range(10):
    ArrayMe += [int(random.random() * 100)]
print(ArrayMe)

MAX = ArrayMe[0]
for i in ArrayMe[1:]:
    if i >= MAX :
        MAX = i
print(MAX)

a = [1,2,5,8,9]
b = a[2:4]
print(b) # [5, 8]


import random

SUITS = ['Club', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

rank = random.choice(RANKS)
suit = random.choice(SUITS)

print(f'{rank} OF {suit}')

#rank = random.randrange(0,len(RANKS))
#suit = random.randrange(0, len(SUITS))

/////////////////////////////////////////////////////////////////////



SUITS = ['Club', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
My_Card = {}
NomeCard = []
for S in SUITS:
    deck = []
    My_Card = {}
    for R in RANKS:
        card = R + ' OF ' + S
        deck += [card]
    My_Card[f'{S}'] = deck
    NomeCard.append(My_Card)
for i in NomeCard:
    print(f'{i} \n')

///////////////////////////////////////////////////////////

b = [1,2,3,4,5,6,7,8,9,10]
n = len(b)
a = [0] * n
for i in range(n):
    n -= 1
    a[i] = b[n]
print(a)


a = a[::-1]
print(a)
print(sum(a))
for x in reversed(a):
    print(x)

/////////////////////////////////////////////////////////////////////////

aliens = []
for aliens_num in range(100000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 99
    new_alien['x'] = 20 * aliens_num
    new_alien['y'] = 0
    aliens.append(new_alien)
num_aliens = len(aliens)
print('Number of aliens created: ')
print(num_aliens)

///////////////////////////////////////////////////////////////


import sys
import random

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
bets = 0
wins = 0

for t in range(trials):
    cash = stake
    while 0 < cash < goal:
        bets += 1
        if random.randrange(0,2): cash += 1
        else: cash -= 1
    if cash == goal: wins += 1

print(str(100 * wins // trials) + ' % wins')
print('Avg # bets: ' + str(bets // trials))

"""