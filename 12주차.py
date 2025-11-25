#과제 32
a = {1, 2, 3, 4, 5}
b = {3, 5, 8, 9, 10}

c = a | b   #합집합
d = a & b   #교집합

print(c)
print(d)

#과제 33
a = {1, 2, 3, 4, 5}
b = {3, 5, 8, 9, 10}

c = a - b
d = a ^ b

print(c)
print(d)

#과제 34
a = {3, 5, 8, 9, 10}
a.update( {100} )

print(a)

#과제 35
a = {100, 200, 300, 400, 500}
a.intersection_update( {400, 500, 600, 700, 800} )
print(a) 

a = {100, 200, 300, 400, 500}
a.difference_update( {400, 500, 600, 700, 800} )
print(a)

a = {100, 200, 300, 400, 500}
a.symmetric_difference_update( {400, 500, 600, 700, 800} )
print(a)

#과제 36
a = {100, 200, 300, 400, 500}
b = {100, 200, 300, 400, 500}

if a == b:
    print("동시")
elif a > b:
    print("상위")
elif a < b:
    print("부분")

#과제 37
a = {9, 12, 15, 17, 22}
a.add(1000)
a.pop()
print(a)

#과제 38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0 }
print(multiples)