'''
@author: Nguyen Van Quyen
Class: K55CLC
MSV: 10020280
'''
import unittest
import decimal
import math
from triangle import *

class Test(unittest.TestCase):
    # Khong la tam giac
    # Ba canh nay khong thoa man tam giac trong mien gia tri
    def test_checkTriangle_1(self):
        self.assertEquals(detect_triangle(1,2,7),"Khong la tam giac")
    # Kiem tra input error
    #Ba canh co 1 canh la ky tu
    def test_checkTriangle_2(self):
        self.assertEquals(detect_triangle("D",2,1),"Error") 
    def test_checkTriangle_3(self):
        self.assertEquals(detect_triangle(1,"D",2),"Error") 
    def test_checkTriangle_4(self):
        self.assertEquals(detect_triangle(1,2,"D"),"Error")
    # Co 1 canh ngoai mien gia tri duoi
    def test_checkTriangle_5(self):
        self.assertEquals(detect_triangle(-1,2,3),"Error")
    def test_checkTriangle_6(self):
        self.assertEquals(detect_triangle(2,-1,3),"Error")
    def test_checkTriangle_7(self):
        self.assertEquals(detect_triangle(2,3,-1),"Error")
    # Co 1 canh ngoai can tren Error
    def test_checkTriangle_8(self):
        self.assertEquals(detect_triangle(2**32, 1, 2),"Error")
    def test_checkTriangle_9(self):
        self.assertEquals(detect_triangle(2,2**32, 1),"Error")
    def test_checkTriangle_10(self):
        self.assertEquals(detect_triangle(2,1,2**32),"Error")
    # Mot trong 3 canh bi NULL
    def test_checkTriangle_11(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_12(self):
        self.assertEquals(detect_triangle(2,3,""),"Error")
    def test_checkTriangle_13(self):
        self.assertEquals(detect_triangle(2,"",3),"Error")
    # Kiem tra tam giac thuong
    def test_checkTriangle_14(self):
        self.assertEquals(detect_triangle(2,3,4),"Tam giac thuong")
    # Kiem tra tam giac can
    def test_checkTriangle_15(self):
        self.assertEquals(detect_triangle(3,3,1),"Tam giac can")
    def test_checkTriangle_16(self):
        self.assertEquals(detect_triangle(2**32 -1 ,3, 2**32 -1),"Tam giac can")
    
    def test_checkTriangle_17(self):
        self.assertEquals(detect_triangle(2**32-1, decimal.Decimal('10')**(-9), 2**32 -1),"Tam giac can")
        
    # Kiem tra tam giac vuong
    def test_checkTriangle_18(self):
        self.assertEquals(detect_triangle(3,4,5),"Tam giac vuong")
    def test_checkTriangle_19(self):
        self.assertEquals(detect_triangle(5,6, math.sqrt(61)),"Tam giac vuong")
    #Kiem tra tam giac vuong can
    def test_checkTriangle_20(self):
        self.assertEquals(detect_triangle(3,3, math.sqrt(18)),"Tam giac vuong can")
    #Kiem tra tam giac deu
    def test_checkTriangle_21(self):
        self.assertEquals(detect_triangle(3,3,3),"Tam giac deu")
    def test_checkTriangle_22(self):
        self.assertEquals(detect_triangle(10**-9, 10**-9, 10**-9),"Tam giac deu")
    def test_checkTriangle_23(self):
        self.assertEquals(detect_triangle(2**32 -1 ,2**32 -1, 2**32 -1),"Tam giac deu")
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()