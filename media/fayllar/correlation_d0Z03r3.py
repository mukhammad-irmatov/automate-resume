import math
import numpy as np
import statistics

students = int(input("Enter number of students: "))
i=1
HS_GPA_list = []
College_GPA_list  = []
while i<=students:
    print(f"Student {i}")
    HS_GPA = float(input("HS GPA: "))
    HS_GPA_list.append(HS_GPA)
    College_GPA = float(input("College GPA: "))
    College_GPA_list.append(College_GPA)
    print("")
    i+=1
#calculating mean of High school gpa list using statistics module
mean_HS_GPA = statistics.mean(HS_GPA_list)
print(f"Mean of High school GPA is {mean_HS_GPA}")
#calculating mean of College school gpa list using statistics module
mean_College_GPA = statistics.mean(College_GPA_list)
print(f"Mean of College GPA is {mean_College_GPA}")
#Calculating square of (xi-x)
X_summ_deviation = 0
x_xi = []
for x in HS_GPA_list:
    x_xi.append(x-mean_HS_GPA)
    squareX = (x-mean_HS_GPA)**2
    X_summ_deviation = X_summ_deviation+squareX

#Calculating square of (xi-x)
Y_summ_deviation = 0
y_yi = []
for y in College_GPA_list:
    y_yi.append(y-mean_College_GPA)
    squareY = (y-mean_College_GPA)**2
    Y_summ_deviation = Y_summ_deviation+squareY

#Calculating S_xx
S_xx = math.sqrt(X_summ_deviation/(students-1))
#Calculating S_yy
S_yy = math.sqrt(Y_summ_deviation/(students-1))
#Calculating S_xy
S_xy = 0
x_xi = np.array(x_xi)
y_yi = np.array(y_yi)
# S_xyM = np.multiply(x_xi,y_yi)
S_xy = np.sum(np.multiply(x_xi,y_yi))/4

#Calculating p value
p = S_xy/(S_xx*S_yy)
print(f"The correlation coefficient is {p}")
if(p>0.9):
    print("strong positive correlation")
elif(p<-0.9):
    print("Strong negative correlation")
elif(p>-0.1 and p<0.1):
    print("no correlation")