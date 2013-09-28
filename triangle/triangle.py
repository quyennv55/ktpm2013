'''
Created on Sep 17, 2013
Test for Triangle
@author: Nguyen Van Quyen
Class: K55CLC
MSV: 10020280
'''
import math

def checkInput(a,b,c):
    if( type(a) in [int, float, long] and type(b) in [float, int, long] and type(c) in [float, int, long]) and checkDoiman(a,b,c):
        return 1;
    elif a is None or b is None or c is None:
        return 0;
    else:
        return 0;       
#Kiem tra dau vao cua 3 canh
def checkDoiman(a,b,c):
        if (a <= 0) or (a > (2**32 - 1)) :
                return 0
        elif (b <= 0) or (b > (2**32 - 1)) :
                return 0
        elif (c <= 0) or (c > (2**32 - 1)) :
                return 0
        else: 
                return 1
# Kiem tra dieu kien cua 1 tam giac thuong
def checkTriangle(a,b,c):
        if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
                return 0
        else:
                return 1
#Kiem tra xem tam giac co deu hay ko   
def checkDeu(a,b,c):
        if(a == b == c) :
            return 1
        else:
            return 0
#Kiem tra xem tam giac co vuong hay ko
def checkCan(a,b,c):
    if(~checkDeu(a,b,c)):
        if(a == b or b==c or c == a ):
            return 1
        else:
            return 0
#Kiem tra xem tam giac co vuong ko hay
def checkVuong(a,b,c):
        if math.fabs(a**2 - b**2 - c**2) <= 10**-9 or math.fabs(b**2 - a**2 - c**2) <= 10**-9 or math.fabs(c**2 - b**2 - a**2) <= 10**-9:
            return 1
        else:
            return 0
#Kiem tra xem tam giac co vuong can ko
def checkVuongCan(a,b,c):
    if checkCan(a,b,c):
        if checkVuong(a,b,c):
            return 1;
        else:
            return 0;
#Kiem tra tong quat
def detect_triangle(a,b,c):
    if checkInput(a,b,c):
            if checkTriangle(a,b,c):
                if checkDeu(a,b,c):
                    return "Tam giac deu"
                elif checkCan(a,b,c):
                    return "Tam giac can"
                elif checkVuong(a,b,c):
                    return "Tam giac vuong"
                else:
                    return "Tam giac thuong"
            else:  
                return "Khong la tam giac" 
    else:
            return "Error"
            

