import numpy as np

a =[

[21.0, 67.0, 88.0, 73.0],
[76.0, 63.0, 7.0, 20.0],
[0.0, 85.0, 56.0, 54.0],
[19.3, 43.0, 30.2, 29.4]
,
]

aResidual =[

[21.0, 67.0, 88.0, 73.0],
[76.0, 63.0, 7.0, 20.0],
[0.0, 85.0, 56.0, 54.0],
[19.3, 43.0, 30.2, 29.4]
,
]

b = [[141.0],
[109.0],
[218.0],
[93.7]]

bResidual = [[141.0],
[109.0],
[218.0],
[93.7]]
size = 4
b = np.float32(b)
a = np.float32(a)


def gaussian(size, a, b):

    j = 0
    o = 0
    j2 = 0
    i = 0
    while i < size: # the row being used to judge
        if i == j and a[i][j] != 1 and a[i][j] != 0:
            divider = a[i][j]

            tempb = b[i][0]
            tempb = tempb / divider
            b[i][0] = tempb
            u = 0
            while u < size:
                temp = a[i][u]
                if temp != 0:
                    temp = temp / divider
                    a[i][u] = temp
                u = u + 1

        while o < size: #the other rows
            if i == o:
                o = o + 1
            else:
                newadder = -1 * a[o][j]

                baddto = b[o][0]
                bmultiply = b[i][0] * newadder
                bsum = baddto + bmultiply
                b[o][0] = bsum

                while j2 < size: # we must do all the additions and subtractions
                        #a[o][j] is the number we want to make 0
                    addto = a[o][j2]
                    multiplyto = a[i][j2]
                    newsum = addto + (newadder * multiplyto)
                    a[o][j2] = newsum
                    j2 = j2 + 1
                j2 = 0
                o = o + 1

        o = 0
        i = i + 1
        j = j + 1

    return b

c = gaussian(size, a, b)
counter = 0
while True:
    aResidual = [

        [21.0, 67.0, 88.0, 73.0],
        [76.0, 63.0, 7.0, 20.0],
        [0.0, 85.0, 56.0, 54.0],
        [19.3, 43.0, 30.2, 29.4]
        ,
    ]

    bResidual = [[141.0],
                 [109.0],
                 [218.0],
                 [93.7]]

    result = [[0],[0],[0],[0]]

    c = np.float64(c)
    aResidual = np.float64(aResidual)

    for i in range(len(aResidual)):

       for j in range(len(c[0])):

           for k in range(len(c)):
               result[i][j] += aResidual[i][k] * c[k][j]

    result = np.float64(result)

    r = [[0], [0], [0], [0]]
    for l in range(len(bResidual)):
        r[l][0] = bResidual[l][0] - result[l][0]

    r = np.float32(r)

    z = gaussian(4, aResidual, r)

    newRe = [[0],[0],[0],[0]]

    for l in range(len(c)):
        newRe[l][0] = c[l][0] + z[l][0]

    loopy = False
    for mk in range(len(c)):
        if newRe[mk][0] == c[mk][0]:
            loopy = True
        else:
            loopy = False
            break

    if loopy == True:
        counter = counter + 1
        break
    else:
        counter = counter + 1
        c = newRe


t = 0
while t < size:
    print(f'X{t} = {c[t][0]}')
    t = t + 1

print(f'I went through this loop {counter} times!')