#1
##import random
##def matrixx(n, m):
##    A = []
##    for i in range(n):
##        A += [[0] * m]
##        for j in range(m):
##            A[i][j] = random.randint(-10, 10)
##    return A
##n = int(input())
##m = int(input())
##A = matrixx(n, m)
##for row in A:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
#a,b
##s = 0
##f = 1
##for row in matrixx(n, m):
##    for i in row:
##        s += abs(i)
##        f *= i ** 2
##print(s, f)

#c
##k = int(input())
##f = 1
##t = 0
##for row in matrixx(n, m):
##    if t == k:
##        for i in row:
##            f *= i
##        print(f)
##        break
##    else:
##        t += 1

#d
##minn = float('+inf')
##sut = 0
##cem = 0
##for i in range(n):
##    for j in range(m):
##        if A[i][j] <= minn:
##            minn = A[i][j]
##            sut = j
##for i in range(n):
##    for j in range(m):
##        if sut == j:
##            cem += A[i][j]
##print(cem)

#e
##def cem(a):
##    s = 0
##    for i in a:
##        s += i
##    return s
##sag = []
##sol = []
##for i in range(n):
##    for j in range(m):
##        if i == j:
##            sol += [A[i][j]]
##for i in range(n):
##    for j in range(m):
##        if i == n - 1 - j:
##            sag += [A[i][j]]
##if cem(sol) > cem(sag):
##    print('sol>sag')
##else:
##    print('sag<sol')


#2
#a
##import random
##def matrixx(n):
##    A = []
##    for i in range(n):
##        A += [[0] * n]
##        for j in range(n):
##            A[i][j] = random.randint(-10, 10)
##    return A
##n = int(input())
##A = matrixx(n)
##B = matrixx(n)
##C1 = []
##C2 = []
##for i in range(n):
##    C1 += [[0] * n]
##    C2 += [[0] * n]
##for i in range(n):
##    for j in range(n):
##        C1[i][j] = A[i][j] + B[i][j]
##        C2[i][j] = A[i][j] - B[i][j]
##print('cem')
##for row in C1:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
##print('ferq')
##for row in C2:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()


#b
##k = int(input('k setir:'))
##m = int(input('m sutun:'))
##C = []
##C1 = []
##C2 = []
##for i in range(n):
##    for j in range(n): 
##        if i == k:
##            C1 += [A[i][j]]
##        if j == m:
##            C2 += [B[i][j]]
##for i in range(n):
##    C += [C1[i] * C2[i]]
##print('c', C)
##print('A')
##for row in A:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
##print('B')
##for row in B:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()

#c
##k = int(input())
##b = []
##b = [0] * n
##b1 = []
##b2 = []
##for i in range(n):
##    b2 += [A[i][i]]
##    for j in range(n):
##        if i == k:
##            b1 += [A[i][j]]
##for i in range(n):
##    b[i] = b1[i] / b2[i]
##for row in A:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
##print(b, b1, b2)

#d
##import random
##def matrixx(n):
##    A = []
##    for i in range(n):
##        A += [[0] * n]
##        for j in range(n):
##            A[i][j] = random.randint(-10, 10)
##    return A
##def cem(A, n):
##    c = 0
##    for i in range(n):
##        for j in range(n):
##            if i == j:
##                c += A[i][j]
##    return c
##n = int(input())
##A = matrixx(n)
##t = cem(A, n)
##for i in range(n):
##    for j in range(n):
##        if i % 2 == 0:
##            A[i][j] = A[i][j] / t
##for row in A:
##    for i in row:
##        print(f'{i:4}', end = '')
##    print()

#e
##import random
##def matrixx(n):
##    A = []
##    for i in range(n):
##        A += [[0] * n]
##        for j in range(n):
##            A[i][j] = random.randint(-10, 10)
##    return A
##n = int(input())
##A = matrixx(n)
##s = 0
##print(A)
##for i in range(n):
##    for j in range(n):
##        s += A[i][j]
##    for t in range(n):
##        A[i][t] = s
##    print(s)
##    s = 0
##print(A)

#3
#a
##import random
##def matrixx(n):
##    A = []
##    for i in range(n):
##        A += [[0] * n]
##        for j in range(n):
##            A[i][j] = random.randint(10, 100)
##    return A
##n = int(input())
##A = matrixx(n)
##maxx = float('-inf')
##for i in range(n):
##    for j in range(n):
##        if A[i][j] >= maxx:
##            maxx = A[i][j]
##            se = i
##            su = j
##print(maxx, se , su)

#b
##import random
##def matrixx(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 100)
##    return a
##n = int(input())
##a = matrixx(n)
##k = 0
##for row in a:
##    for i in row:
##        print(f'{i:4}', end = '')
##    print()
##for j in range(n):
##    for i in range(n//2):
##        a[i][j], a[n - 1 - i][j] = a[n - 1 - i][j], a[i][j]
##print('a')
##for row in a:
##    for i in row:
##        print(f'{i:4}', end = '')
##    print()

#c
##import random
##def matrixx(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 100)
##    return a
##def pronic(z):
##    for i in range(z):
##        if i * (i + 1) == z:
##            return 'true'
##    return 'false'
##n = int(input())
##a = matrixx(n)
##listt = []
##for i in range(n):
##    for j in range(n):
##        if i % 2 == 0 and pronic(a[i][j]) == 'true':
##            listt += [a[i][j]]
##print(listt)

#d
##import random
##def matrixx(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 100)
##    return a
##def sade(a):
##    s = 0
##    for i in range(1, a + 1):
##        if a % i == 0:
##            s += 1
##    if s == 2:
##        return 'true'
##    else:
##        return 'false'
##n = int(input())
##a = matrixx(n)
##listt = []
##for i in range(n):
##    for j in range(n):
##        if (i == j or i == n - 1 - j) and sade(a[i][j]) == 'true':
##            listt += [a[i][j]]
##print(listt)

#4
#a
##import random
##def create_matrix(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 99)
##    return a
##n = int(input())
##a = create_matrix(n)
##s = 0
##count = 0
##for i in range(n):
##    for j in range(n):
##        s += a[i][j]
##        count += 1
##edor = s / count
##print(edor)
##for i in range(n):
##    for j in range(n):
##        if a[i][j] < edor:
##            a[i][j] = 0
##        else:
##            a[i][j] = 255
##for row in a:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()


#b
##import random
##def create_matrix(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 99)
##    return a
##n = int(input())
##a = create_matrix(n)
##for i in range(n):
##    for j in range(i + 1):
##        if a[j][i] > 50:
##            a[j][i] = 255
##        else:
##            a[j][i] = 0
##for row in a:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()

#c
##import random
##def create_matrix(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 99)
##    return a
##n = int(input())
##a = create_matrix(n)
##for i in range(n):
##    for j in range(i + 1):
##        a[j][i] = 0
##for row in a:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()

#f
##import random
##def create_matrix(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 99)
##    return a
##n = int(input())
##a = create_matrix(n)
##s = []
##for i in range(n):
##    s += [[0] * n]
##for i in range(n):
##    for j in range(n):
##        s[i][j] = a[n - 1 - j][i]
##for row in a:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
##print('s')
##for row in s:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()

#5
##import random
##def create_matrix(n):
##    a = []
##    for i in range(n):
##        a += [[0] * n]
##        for j in range(n):
##            a[i][j] = random.randint(10, 20)
##    return a
##n = int(input())
##a = create_matrix(n)
#5(1)
##for i in range(n):
##    for j in range(n):
##        if j == 0 or j == n - 1:
##            a[i][j] = 5
##        a[i][i] = 5
#5(2)
##for i in range(n):
##    for j in range(n):
##        if j == 0 or j == n - 1 or i == n // 2 or i == 0:
##            a[i][j] = 5
#5(3)
##for i in range(n // 2 + 1):
##    for j in range(n):
##        a[i][i] = 5
##        a[i][n - i - 1] = 5
##for i in range(n):
##    for j in range(n):
##        if i > n // 2 and j == n // 2:
##            a[i][j] = 5
#5(4)
##for i in range(n):
##    for j in range(n):
##        if i == 0 or j == n // 2:
##            a[i][j] = 5
#5(5)
##for i in range(n):
##    for j in range(n):
##        if i == 0 or i == n - 1:
##            a[i][j] = 5
##        a[i][n - 1 - i] = 5
#5(6)
##for i in range(n):
##    for j in range(n):
##        if j == 0 or j == n - 1 or i == 0 or i == n - 1:
##            a[i][j] = 5
##for row in a:
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()




####DICTIONARY

#1
##dict = { 
##'Asia': 
##{ 'population': 4545133094, 'area': 31033131 }, 
##'Africa': 
##{ 'population': 1287920518, 'area': 29648481 }, 
##'Europe': 
##{ 'population': 742648010, 'area': 22134900 }, 
##'North America': 
##{ 'population': 587615976, 'area': 21329926 }, 
##'South America': 
##{ 'population': 428240515, 'area': 17461112 }, 
##'Australia/Oceania': 
##{ 'population': 41261212, 'area': 8486460 }, 
##'Antarctica':	 
##{ 'population': 0, 'area': 13720000 } 
##} 
##
##new = {}
##for i in dict:
##    if dict[i]['population'] > 1000000000:
##        new[i] = dict[i]
##print(new)

#2
##users = {
##    'maximus' : 'password1',
##    'asterix' : 'password2',
##    'starrex' : 'password3'
##    }
##ad = input()
##sifre = input()
##if ad in users.keys():
##    if sifre in users.values():
##        print('salam, xos gelmissiniz')
##    else:
##        print('sifre yanlisdir')
##else:
##    print('ad yanlisdir')

#3
##a = input()
##son = {}
##for herf in a:
##    if not herf in son:
##        son[herf] = 1
##    else:
##        son[herf] += 1
##print(son)

#4
##verilen = {
##    'n1' : 'gmc',
##    'n2' : 'bmw',
##    'n3' : 'kia',
##    'n4' : 'bmw',
##    'n5' : 'audi'
##    }
##son = {}
##listt = []
##for i in verilen:
##    if not verilen[i] in listt:
##        listt += [verilen[i]]
##        son[i] = verilen[i]
##print(son)

#5
##data = {
##    'robert': {'IELTS': 9.0, 'IKT':98, 'Giris_bali': 690}, 
##    'juliet': {'IELTS': 7.0, 'IKT':100, 'Giris_bali': 650},
##    'tom':  {'IELTS': 6.5, 'IKT':89, 'Giris_bali': 640}
##    }
##minni = float('-inf')
##minnt = float('-inf')
##son = []
##for i in data:
##    if data[i]['IELTS'] > minni:
##        minni = data[i]['IELTS']
##        a1 = i
##    if data[i]['IKT'] > minnt:
##        minnt = data[i]['IKT']
##        a2 = i
##son = [a1] + [a2]
##print(son)






























