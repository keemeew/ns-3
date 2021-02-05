import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

f1 = open('dctcp-example-t1-length.dat', 'r')
f2 = open('dctcp-example-t2-length.dat', 'r')

r1 = f1.readlines()
r2 = f2.readlines()

x1 = []
y1 = []
y2 = []
y3 = []
y4 = []

for i in range(1,102):
    x1.append(float(r1[i].split()[0]))

    y1.append(float(r1[i].split()[1]))
    y2.append(float(r2[i].split()[1]))

    y3.append(float(r1[i].split()[2]))
    y4.append(float(r2[i].split()[2]))

avg1 = sum(y1,0.0) / len(y1)
avg2 = sum(y2,0.0) / len(y2)
avg3 = sum(y3,0.0) / len(y3)
avg4 = sum(y4,0.0) / len(y4)
print(avg1)
print(avg2)
print(avg3)
print(avg4)
plt.xticks()
plt.plot(x1, y1, label = 'Switch T1')
plt.plot(x1, y2, label = 'Switch T2')
plt.legend()
plt.ylabel('Queue length (pkts)')
plt.xlabel('Time')
plt.savefig('qlen_pkts.png')

plt.clf()

plt.plot(x1, y3, label = 'Switch T1')
plt.plot(x1, y4, label = 'Switch T2')
plt.legend()
plt.ylabel('Queue length (us)')
plt.xlabel('Time')
plt.savefig('qlen_us.png')

