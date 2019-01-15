#Q1
s = 'This line will be appended to a file'
f = open('test.txt', 'a')
f.write(s)
f.close()

#Q3
#A) 5
#B) "divisor is not a good choice"

#Q4
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [11, 45, 23, 33, 89, 90, 22, 54, 67]
plt.plot(x, y, label = 'Line1')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('x-y graph')
plt.show()

#Q5
(24, 4)
(4, 0)
(4)

#Q6
class Employee:
    def __init__(self, name, job, salary, age):
        self.name = name
        self.job = job
        self.salary = salary
        self.age = age

    def pay_increase(self, percent):
        self.salary = self.salary*(1+percent/100)

#Q7
('Charlie', 'dev', '110')

#Q8
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = 3*2[i][j]
i = 0, 1, 2
j = 0, 1, 2, 3

OR

import numpy as np
b = np.array(a)
b = b*3

#Q9
[0, 0, 0]
[0, 2, 4]
[0, 4, 8]
[0, 6, 12]
# second range determines number of rows

#Q10
import numpy as np
n = 5
a = np.zeros((n, n))
a[1:4, 1:3,] = 9

#Q11
[12, 1]
[8, 15]
[10, 7]

#Q12
import re
matches = re.finall(r'\b[Ss] \w*'a)
print(matches)

#Q13
pattern = r'\S{3}_a{2, 3}\d*'

#Q14
(y nam)

#Q15
def ffo(s, x):
    i = 0
    while i<len(s):
        return i
    return -1

###DAY TWO

######Problem 4
class StudentInfoHolder:
    def __init__(self):

    def add_student(self, id, name, grade):

        if (id in self.info)
            raise Exception('No Dupes')
         elif

#####Problem 5
import matplotlib.pyplot as plt

heights = [65, 67, 65, 64, 69, 67, 66, 61, 72, 68]
seconds = [265, 341, 290, 275, 291, 361, 309, 264, 390, 278]
plt.plot(heights, seconds, '+', color='g')
plt.title('Run The Mile')
plt.xlabel('Heights')
plt.ylabel = ('Seconds')
plt.show()

########Problem 6
def addUp(num):
    if num == 1
      return 1
    else:
        return num + addUp(num - 1)



#########Problem 7
import numpy as np
matrix = np.ones((5, 5))
matrix[1:4, 1:4] = 2
matrix[2, 2] = 3














