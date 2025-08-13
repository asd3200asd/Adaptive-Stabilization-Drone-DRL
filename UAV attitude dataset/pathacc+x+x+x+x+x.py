import numpy as np
import matplotlib.pyplot as plt

import scipy.integrate as integral

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

np0 = np.genfromtxt('10-0-10.csv', delimiter=',')

np1 = np.genfromtxt('10-1-10.csv', delimiter=',')
np2 = np.genfromtxt('10-2-10.csv', delimiter=',')
np3 = np.genfromtxt('10-3-10.csv', delimiter=',')
np4 = np.genfromtxt('10-4-10.csv', delimiter=',')
np5 = np.genfromtxt('10-5-10.csv', delimiter=',')
np6 = np.genfromtxt('10-6-10.csv', delimiter=',')
np7 = np.genfromtxt('10-7-10.csv', delimiter=',')
np8 = np.genfromtxt('10-8-10.csv', delimiter=',')
np9 = np.genfromtxt('10-9-10.csv', delimiter=',')
np10 = np.genfromtxt('10-10-10.csv', delimiter=',')




time1=np0[200:350, 3]*-1-4.67
data = np0[200:350, 1]*-1-80

plt.plot(data, time1, label=' $a_{i}^k$ = -10 $\mathregular{m^2}$/s')

time1=np1[200:350, 3]*-1-4.67
data = np1[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 9 $\mathregular{m^2}$/s')

time1=np2[200:350, 3]*-1-4.67
data = np2[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 8 $\mathregular{m^2}$/s')

time1=np3[200:350, 3]*-1-4.67
data = np3[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 7 $\mathregular{m^2}$/s')

time1=np4[200:350, 3]*-1-4.67
data = np4[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 6 $\mathregular{m^2}$/s')


time1=np5[200:350, 3]*-1-4.67
data = np5[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 5 $\mathregular{m^2}$/s')

time1=np6[200:350, 3]*-1-4.67
data = np6[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 4 $\mathregular{m^2}$/s')

time1=np7[200:350, 3]*-1-4.67
data = np7[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 3 $\mathregular{m^2}$/s')

time1=np8[200:350, 3]*-1-4.67
data = np8[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 2 $\mathregular{m^2}$/s')

time1=np9[200:350, 3]*-1-4.67
data = np9[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ = - 1 $\mathregular{m^2}$/s')

time1=np10[200:350, 3]*-1-4.67
data = np10[200:350, 1]*-1-80
plt.plot(data, time1, label='$a_{i}^k$ =  0 $\mathregular{m^2}$/s')




'''

np1 = np.genfromtxt('1-1-1.csv', delimiter=',')
np2 = np.genfromtxt('1-2-1.csv', delimiter=',')
np3 = np.genfromtxt('1-3-1.csv', delimiter=',')
np4 = np.genfromtxt('1-4-1.csv', delimiter=',')
np5 = np.genfromtxt('1-5-1.csv', delimiter=',')
np6 = np.genfromtxt('1-6-1.csv', delimiter=',')
np7 = np.genfromtxt('1-7-1.csv', delimiter=',')
np8 = np.genfromtxt('1-8-1.csv', delimiter=',')
np9 = np.genfromtxt('1-9-1.csv', delimiter=',')
np10 = np.genfromtxt('1-10-1.csv', delimiter=',')
np11 = np.genfromtxt('1-11-1.csv', delimiter=',')



time1=np1[180:700, 3]*-1-5
data = np1[180:700, 1]*-1-9

plt.plot(data, time1, label='$a_{i}^k$ = 0 $\mathregular{m^2}$/s')

time1=np2[180:700, 3]*-1-5
data = np2[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 1 $\mathregular{m^2}$/s')

time1=np3[180:700, 3]*-1-5
data = np3[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 2 $\mathregular{m^2}$/s')

time1=np4[180:700, 3]*-1-5
data = np4[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 3 $\mathregular{m^2}$/s')


time1=np5[180:700, 3]*-1-5
data = np5[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 4 $\mathregular{m^2}$/s')

time1=np6[180:700, 3]*-1-5
data = np6[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 5 $\mathregular{m^2}$/s')

time1=np7[180:700, 3]*-1-5
data = np7[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 6 $\mathregular{m^2}$/s')

time1=np8[180:700, 3]*-1-5
data = np8[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 7 $\mathregular{m^2}$/s')

time1=np9[180:700, 3]*-1-5
data = np9[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 8 $\mathregular{m^2}$/s')

time1=np10[180:700, 3]*-1-5
data = np10[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ = 9 $\mathregular{m^2}$/s')

time1=np11[180:700, 3]*-1-5
data = np11[180:700, 1]*-1-9
plt.plot(data, time1, label='$a_{i}^k$ =10 $\mathregular{m^2}$/s')
'''


plt.title("The Deceleration Flight Trajectory")
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
#plt.legend(bbox_to_anchor=(1.2, 1))
plt.legend(bbox_to_anchor=(1.02, 1))

#plt.xlim(-1,70)
#plt.ylim(-1.0,1.7)


plt.tight_layout()
plt.savefig("pathacc-x.svg", dpi = 400)

plt.show()
