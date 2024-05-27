# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista_numere = [i for i in range(1, 11)]
print(lista_numere)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for numar in lista_numere:
    if numar % 2 == 0:
        print(numar)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
persoana = {'nume': 'John', 'age': 30, 'city': 'New York'}
for cheie, valoare in persoana.items():
    print(f'{cheie}: {valoare}')
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for rand in matrice:
    for element in rand:
        print(element, end=' ')
    print()
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
secventa = range(1, 11)
for numar in secventa:
    print(numar)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for index, valoare in enumerate(lista_numere):
    print(f'Index: {index}, Valoare: {valoare}')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
for numar, caracter in zip(lista1, lista2):
    print(f'{numar} -> {caracter}')
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista_numere = [i for i in range(1, 11)]
print(lista_numere)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
lista_numere = [1, 2, 3, 4, 5]
while lista_numere[0] <= 50:
    lista_numere = [x * 2 for x in lista_numere]
print(lista_numere)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
patrate_perfecte = [x**2 for x in range(1, 11)]
print(patrate_perfecte)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
    print(f'7 x {i} = {7 * i}')
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
perechi = [[(i, j) for j in range(1, 6)] for i in range(1, 6)]
for pereche in perechi:
    print(pereche)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for pereche in perechi:
    for (i, j) in pereche:
        if i < j:
            print(f'({i}, {j})')
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
import random
lista_random = [random.randint(1, 20) for _ in range(10)]
print(f'Lista random: {lista_random}')
gasit = False
index = 0
while index < len(lista_random) and not gasit:
    if lista_random[index] > 10:
        print(f'Prima valoare mai mare decât 10 este: {lista_random[index]}')
        gasit = True
    index += 1
if not gasit:
    print("Nu există valori mai mari decât 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Dimensiunea pătratului: "))
for i in range(dimensiune):
    for j in range(dimensiune):
        print('*', end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
sir = "abcdefg"
for i in range(len(sir)):
    print(sir[i:])
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
randuri = 8
coloane = 15
for i in range(randuri):
    for j in range(coloane):
        if (i + j) % 2 == 0:
            print('+', end='')
        else:
            print('-', end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
inceput = 3
for i in range(1, 6):
    for j in range(i):
        print(inceput**(j+1), end=' ')
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print(inceput**(j+1), end=' ')
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.