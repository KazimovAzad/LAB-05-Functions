#4
##def yoxla(a):
##    n = 1
##    while a >= n * (n + 1):
##        if a == n * (n + 1):
##            return 'pronic'
##        n += 1
##    return 'heteromecic'
##p = int(input())
##print(yoxla(p))

#5
##def lenn(a):
##    s = 0
##    while a > 0:
##        a //= 10
##        s += 1
##    return s
##a = int(input())
##print(lenn(a))

#6
##def lenn(a):
##    s = 0
##    while a > 0:
##        a //= 10
##        s += 1
##    return s
##def disarium(a):
##    s = 0
##    copy = a
##    i = lenn(a)
##    while a > 0:
##        s += (a % 10) ** i
##        a = a // 10
##        i -= 1
##    if copy == s:
##        return 'disarium'
##    else:
##        return 'deyil'
##a = int(input())
##print(disarium(a))
    
#7
##def curzon(a):
##    if (2 ** a + 1) % (2 * a + 1) == 0:
##        return 'curzon'
##    else:
##        return 'deyil'
##a = int(input())
##print(curzon(a))

#8
##def kempner(a):
##    f = 1
##    i = 1
##    while i != a:
##        f *= i
##        if f % a == 0:
##            return i
##        i += 1
##    return a
##a = int(input())
##print(kempner(a))

#9
##def sade(a):
##    s = 0
##    for i in range(1, a + 1):
##        if a % i == 0:
##            s += 1
##    if s == 2:
##        return 'he'
##    else:
##        return 'yox'
##def moran(a):
##    s = 0
##    copy = a
##    while a > 0:
##        s += a % 10
##        a = a // 10
##    if sade(copy // s) == 'he':
##        return 'moran'
##    else:
##        return 'non-moran'
##a = int(input())
##print(moran(a))

#10
##def lenn(a):
##    s = 0
##    while a > 0:
##        a //= 10
##        s += 1
##    return s
##def yoxla(a):
##    copy = a
##    while copy > 10:
##        k = copy % 10
##        copy //= 10
##    a_1 = k
##    a_son = a % 10
##    if (a_son + a_1)**0.5 > 3:
##        return True
##    else:
##        return False
##a = int(input())
##print(yoxla(a))

#11
##def qars_sade(a,b):
##    s = 0
##    if a > b:
##        for i in range(2, b + 1):
##            if a % i == 0 and b % i == 0:
##                return False
##        return True
##    else:
##        for i in range(2, a + 1):
##            if a % i == 0 and b % i == 0:
##                return False
##        return True
##a = int(input())
##b = int(input())
##print(qars_sade(a, b))
                
#12
##def sade(a):
##    s = 0
##    for i in range(1, a + 1):
##        if a % i == 0:
##            s += 1
##    if s == 2:
##        return 'yes'
##    else:
##        return 'no'
##def hiper(a):
##    if sade(a) == 'yes':
##        while a > 0:
##            a //= 10
##            if a != 0 :
##                if sade(a) == 'no':
##                    return False
##        return True
##    else:
##        return False
##a = int(input())
##print(hiper(a))

#13
##def ek_eb(a, b):
##    while a != b:
##        if a > b:
##            a = a - b
##        else:
##            b = b - a
##    return a
##a = int(input())
##b = int(input())
##print('ebob', ek_eb(a, b))
##print('ekob', a * b // ek_eb(a, b))

#14
##def artan(a, b, c):
##    if a > b:
##        if b > c:
##            print(c)
##            print(b)
##            return a
##        
##        else:
##            if a > c:
##                print(c)
##                print(b)
##                return a
##            else:
##                print(b)
##                print(a)
##                return c
##    elif a < b:
##        if c > b:
##            print(a)
##            print(b)
##            return c
##        else:
##            if a > c:
##                print(c)
##                print(a)
##                return b
##            else:
##                print(a)
##                print(c)
##                return b
##a = int(input())
##b = int(input())
##c = int(input())
##print(artan(a, b, c))
                
#15
##def ebob(a, b):
##    while a != b:
##        if a > b:
##            a = a - b
##        else:
##            b = b - a
##    return a
##a = int(input())
##b = int(input())
##print(a// ebob(a, b),'/', b//ebob(a, b))

#16
##def ters(a):
##    son = 0
##    while a > 0:
##        son = son * 10 + a % 10
##        a //= 10
##    return son
##a = int(input())
##print(ters(a))










