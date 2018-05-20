import json
import math
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\Илюша\\Desktop\\fde6ef45-0d3d-432f-8082-8f0baa5e5249.json'
f = open(path, 'r')
i = 0
lat = []
lon = []
lat_res = []
lon_res = []
dist = [0, 0, 0, 0, 0, 0]
R = 6371

dLat = 0
dLon = 0
prom = 0
c = 0
d = 0
m = 0


def localparse(s):
    i = s.find('"')
    j = s.find(':')
    s2 = s[i + 1:(j - 1)]
    val = s[j + 1:]
    s2 = s2.strip()
    val = float(val.strip())
    if s2 == "lng":
        lon.append(val)
    if s2 == "lat":
        lat.append(val)
    return [s2, val]


def parse(s):
    i = 0
    j = 0
    while (i != -1) and (j != -1):

        i = s.find('"')
        j = s.find(',')
        s2 = s[i:j]
        s = s[j + 1:]
        if j == -1:
            t = s2.find("}")
            s2 = s2[:t]
        localparse(s2)

s = f.readline()
while s != "":
    parse(s)
    s = f.readline()

size = len(lat)
plt.figure()
plt.plot(lat, lon)
plt.show()
i = 0
while i < 6:
    lat_res.append(lat[i])
    lon_res.append(lon[i])  # начальное заполнение итоговых векторов
    i = i + 1
i = 6
j = 0
k = 0
flag = 0
flag2 = 0
while i < size - 6:
    j = 0
    while j <= len(lat_res) - 6:
        k = 0
        while k < 6:
            if k!=6:
                c2 = math.cos(lat[i + 1])
                c1 = math.cos(lat[i])
                s2 = math.sin(lat[i + 1])
                s1 = math.sin(lat[i])
                delt = lon[i + 1] - lon[i]
                y = math.sqrt(math.pow(c * math.sin(delt), 2) + math.pow(c1 * s2 - s1 * c2 * math.cos(delt), 2))
                x = s1 * s2 + c1 * c2 * math.cos(delt)
                ad = math.atan2(y, x)
                dist = ad * R
                if dist > 300:
                    flag = 5
                    break

            c2 = math.cos(lat_res[j + k])
            c1 = math.cos(lat[i + k])
            s2 = math.sin(lat_res[j + k])
            s1 = math.sin(lat[i + k])
            delt = lon_res[j + k] - lon[i + k]
            y = math.sqrt(math.pow(c * math.sin(delt), 2) + math.pow(c1 * s2 - s1 * c2 * math.cos(delt), 2))
            x = s1 * s2 + c1 * c2 * math.cos(delt)
            ad = math.atan2(y, x)
            dist = ad * R
            if dist < 5:
                flag = flag + 1
            k = k + 1
        k = 0
        if flag >= 2:
            break
        j = j + 1
    if flag <= 2:
        k = 0
        while k < 6:
            lat_res.append(lat[i + k])
            lon_res.append(lon[i + k])
            k = k + 1
    flag = 0
    i = i + 6
    if i % 100 == 0:
        print(i)
print("Result")
print(size)
print(len(lat_res))
plt.figure()
plt.plot(lat_res, lon_res)
plt.show()
