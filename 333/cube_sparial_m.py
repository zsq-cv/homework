def calculate_step(num):
    layer = 0
    initial=0
    if num==1:
        return 0
    else:
        initial = 0
        layer = 0
        if num == 1:
            return 0
        else:
            num_cal_layer = num - 1
            while num_cal_layer > initial:
                num_cal_layer = num_cal_layer - initial
                initial = initial + 8
                layer = layer + 1
        vertical = 0
        count=2*layer+1
        mid1=count*count-layer
        mid2=count*count-layer*3
        mid3=count*count-layer*5
        mid4=count*count-layer*7
        list=[abs(num-mid1),abs(num-mid2),abs(num-mid3),abs(num-mid4)]
        vertical=min(list)
    return layer+vertical
def min(list):
    min=list[0]
    for i in list:
        if i<=min:
            min=i
    return min
assert(calculate_step(5) == 2)
assert(calculate_step(17) == 4)
assert(calculate_step(25) == 4)
assert(calculate_step(57) == 8)
assert(calculate_step(100000) == 173)
assert (calculate_step(2345678) == 1347)
print('Congratulations, you\'ve passed all of the cases!')
