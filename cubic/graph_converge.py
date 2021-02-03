count = 0
line1 = []
intro1 = ''
intro2 = ''

r1 = open('cubic-cwnd.log', 'r')
r2 = open('newreno-cwnd.log', 'r')
r3 = open('cubic-ssthresh.log', 'r')
r4 = open('newreno-ssthresh.log', 'r')
w1 = open('cwnd_compare', 'w')
w2 = open('ssthresh_compare', 'w')

intro1 = "set title 'CWND of Cubic and Newreno'\nset xlabel 'Time (s)'\nset ylabel 'CWND'\nset xrange [0:600]\nplot '-'  title 'Cubic' with lines, '-' title 'Newreno' with lines\n"
intro2 = "set title 'SSTHRESH of Cubic and Newreno'\nset xlabel 'Time (s)'\nset ylabel 'SSTRESH'\nset xrange [0:600]\nplot '-' title 'Cubic' with lines, '-' title 'Newreno' with lines\n"

w1.write(intro1)

while True:
    count += 1
    line1 = r1.readline()
    if count > 5:
        w1.write(line1)
        if not line1: break
            
count = 0
w1.write('e\n')

while True:
    count += 1
    line1 = r2.readline()
    if count > 5:
        w1.write(line1)
        if not line1: break

count = 0            
w2.write(intro2)

while True:
    count += 1
    line1 = r3.readline()
    if count > 5:
        w2.write(line1)
        if not line1: break
            
count = 0
w2.write('e\n')

while True:
    count += 1
    line1 = r4.readline()
    if count > 5:
        w2.write(line1)
        if not line1: break            


