def number_find(num):
    list=[]
    while num%2 == 0:
        num=num/2
        list.append(2)
    while num%3 == 0:
        num=num/3
        list.append(3)
    while num%5 == 0:
        num=num/5
        list.append(5)
    if num == 1:
        return list
    else:
        return None
assert(number_find(1845281250) == [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5])
assert(number_find(3690562500) == [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5])
assert(number_find(1230187500) == [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5])
assert(number_find(10023750) == None)
print('Congratulations, you\'ve passed all of the cases!')
