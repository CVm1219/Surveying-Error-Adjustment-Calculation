import math


radian = []
lnsin = []
d = []


for i in range(8):
    
    theta = 0

    for j in range(6):
        a, b, c = map(float, input(f"θ{i + 1}, {j + 1} > ").split())
        degree = a * 60 * 60 + b * 60 + c
        rad = degree / (360 * 60 * 60) * 2 * math.pi
        theta += rad
    theta /= 6

    radian.append(theta)
    lnsin.append(math.log(math.sin(theta)))
    d.append(1 / math.tan(theta))


print("radian")
print(radian)
print("lnsin")
print(lnsin)
print("d")
print(d)


cnt = 0
while True:
    cnt += 1
    print(f"{cnt}回目")

    w1 = -1 * math.pi * 2
    for i in range(8):
        w1 += radian[i]
    
    w2 = radian[0] + radian[1] - radian[4] - radian[5]

    w3 = radian[2] + radian[3] - radian[6] - radian[7]

    p = 1
    w4 = 0
    a1 = 0
    for i in range(8):
        w4 += p * lnsin[i]
        a1 += p * d[i]
        p *= -1

    a2 = d[0] - d[1] - d[4] + d[5]

    a3 = d[2] - d[3] - d[6] + d[7]

    a4 = 0
    for i in range(8):
        a4 += d[i] ** 2

    lambda4 = -1 * (w4 - a1 * w1 / 8 - a2 * w2 / 4 - a3 * w3 / 4) / (a4 - a1 ** 2 / 8 - a2 ** 2 / 4 - a3 ** 2 / 4)
    lambda1 = -1 * (w1 - a1 * lambda4) / 8
    lambda2 = -1 * (w2 - a2 * lambda4) / 4
    lambda3 = -1 * (w3 - a3 * lambda4) / 4

    print(f"w1 = {w1}")
    print(f"w2 = {w2}")
    print(f"w3 = {w3}")
    print(f"w4 = {w4}")
    print(f"lambda1 = {lambda1}")
    print(f"lambda2 = {lambda2}")
    print(f"lambda3 = {lambda3}")
    print(f"lambda4 = {lambda4}")

    v = []
    sum_v = 0
    v.append(lambda1 + lambda2 + d[0] * lambda4) 
    v.append(lambda1 + lambda2 - d[1] * lambda4)
    v.append(lambda1 + lambda3 + d[2] * lambda4)
    v.append(lambda1 + lambda3 - d[3] * lambda4)
    v.append(lambda1 - lambda2 + d[4] * lambda4)
    v.append(lambda1 - lambda2 - d[5] * lambda4)
    v.append(lambda1 - lambda3 + d[6] * lambda4)    
    v.append(lambda1 - lambda3 - d[7] * lambda4)
    print("v")
    print(v)

    for i in range(8):
        radian[i] += v[i]
    print("M-radian")
    print(radian)

    degree = []
    for i in range(8):
        degree.append(radian[i] / (2 * math.pi) * 360 * 60 * 60)

    lnsin.clear()
    d.clear()
    print("M-degree")
    for i in range(8):
        deg1 = int(degree[i] / 60 / 60)
        deg2 = int(degree[i] / 60) - deg1 * 60
        deg3 = degree[i] - deg1 * 60 * 60 - deg2 * 60

        print(f"{deg1}°{deg2}'{deg3}")

        lnsin.append(math.log(math.sin(theta)))
        d.append(1 / math.tan(theta))
    
    flag = True
    limit = 1. / 10**8
    for i in range(8):
        if v[i] > limit:
            flag = False
            break

    if flag:
        break

input()