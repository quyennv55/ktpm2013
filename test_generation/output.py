'''
Created on Oct 7, 2013
@author: Nguyen Van Quyen
@Class: K55CLC
@MSV: 10020280
'''
import itertools
from input import *
import unittest
# Kiem tra xem gia tri vao co phai int hay khong
def checkDoiman(a):
    if a < (-2**32 -1) or a > (2**32 -1):
        return 0;
    else:
        return 1;  
# Ham doi cho a va b
def swap(a,b):
    return b, a

#Kiem tra xem co phai lop tuong duong manh khong
def checkClasses(a = []):
    for element in a:
        min = []
        max = []
        for elmt in element:
            if checkValid(elmt[0], elmt[1]) is 0:
                return 0
                break
            if checkDoiman(int(elmt[0])) is 0 or checkDoiman(int(elmt[1])) is 0:
                return 0
                break
            min.append(elmt[0])
            max.append(elmt[1])
        for i in range(0, len(min)):
            for j in range(i+1, len(min)):
                if max[j] < max[i]:
                    max[j], max[i] = swap(max[j], max[i])
                    min[j], min[i] = swap(min[j], min[i])
        for i in range(0, len(min)-1):
            if int(min[i+1]) < int(min[i]):
                return 0
                break
            if int(max[i]) >= int(min[i+1]):
                return 0
                break
    return 1
#Kiem tra xem [a;b] co phai khoang tang hay ko
def checkValid(a,b):
    if a > b:
       return 0
    return 1
# Ham xu ly tach cac doan tu comment dau vao
def readInput():
    #Get Comments as doc in Python
    stgComments = main.__doc__
    # Each line in Comment respectively
    List = stgComments.split('\n')
    #Delete a element at start of comment
    List.pop(0)
    #Delete a element at end of comment
    List.pop()
    # Each Line in Comments
    Lists = []
    for list in List:
        a = []
        temp =''
        temp = temp +list[list.find('[')+1:]
        sections  = temp.split('[')
        for section in sections:
            sect = ''
            sect = section[: -1]
            array = sect.split(';')
            a.append(array)
        Lists.append(a)
    return Lists

#Ham sinh cac bo test case tu comment dau vao
def makeTests():
    list = readInput()
    list1 = []
    testList=[]
    for i in list:
        list2= []
        for j in i: 
            ave = (int(j[0]) + int(j[1]))/2
            list2.append(ave)
        list1.append(list2)
    for element in itertools.product(*list1):
        testList.append(element)
    return testList

#Dua ra Exception neu dau vao loi
if checkClasses(readInput()) is 0:
    raise Exception("wrong input");

# Ham test tu dong
class TestSequense(unittest.TestCase):
    pass
    
def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    list = makeTests()
    for i in range(0,len(list)):
        test_name = 'test_Auto_%s' %i
        test = test_generator(main(*list[i]),None)
        setattr(TestSequense, test_name, test)
    unittest.main()