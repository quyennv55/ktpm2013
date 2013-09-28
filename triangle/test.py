import unittest
import decimal
import math
from triangle import *

class Test(unittest.TestCase):
    #Test khong phai la tam giac
    def test_checkTriangle_1(self):
        self.assertEquals(detect_triangle(1,2,7),"Khong la tam giac")
    def test_checkTriangle_2(self):
        self.assertEquals(detect_triangle(7,2,1),"Khong la tam giac") 
    def test_checkTriangle_3(self):
        self.assertEquals(detect_triangle(1,7,2),"Khong la tam giac")
    #Test cac canh dau vao khong thoa man
    #Mot trong cac canh la kieu char 
    def test_checkTriangle_4(self):
        self.assertEquals(detect_triangle("D",2,3),"Error") 
    def test_checkTriangle_5(self):
        self.assertEquals(detect_triangle(2,"D",3),"Error")
    def test_checkTriangle_6(self):
        self.assertEquals(detect_triangle(2,3,"D"),"Error")
    #Mot trong cac canh co do dai 0
    def test_checkTriangle_7(self):
        self.assertEquals(detect_triangle(0,2,3),"Error")
    def test_checkTriangle_8(self):
        self.assertEquals(detect_triangle(2,3,0),"Error")
    def test_checkTriangle_9(self):
        self.assertEquals(detect_triangle(2,0,3),"Error")
    #Mot trong cac canh co bien
    def test_checkTriangle_10(self):
        self.assertEquals(detect_triangle(2**32 - 1,3,5),"Khong la tam giac")
    def test_checkTriangle_11(self):
        self.assertEquals(detect_triangle(3,2**32 -1,5),"Khong la tam giac")
    def test_checkTriangle_12(self):
        self.assertEquals(detect_triangle(3,5, 2**32 -1),"Khong la tam giac")
    # Ngoai khoang gioi han
    def test_checkTriangle_13(self):
        self.assertEquals(detect_triangle(-1,2,3),"Error")
    def test_checkTriangle_14(self):
        self.assertEquals(detect_triangle(2,-1,3),"Error")
    def test_checkTriangle_15(self):
        self.assertEquals(detect_triangle(2,3,-1),"Error")
    def test_checkTriangle_16(self):
        self.assertEquals(detect_triangle(2**32 ,3,1),"Error")
    def test_checkTriangle_17(self):
        self.assertEquals(detect_triangle(2,2**32,1),"Error")
    def test_checkTriangle_18(self):
        self.assertEquals(detect_triangle(2,3,2**32),"Error")
    #Mot trong cac canh co gia tri rong or null
    
    def test_checkTriangle_19(self):
        self.assertEquals(detect_triangle(2,3,""),"Error")
    def test_checkTriangle_20(self):
        self.assertEquals(detect_triangle(2,"",3),"Error")
    def test_checkTriangle_21(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
  
    # Kiem tra tam giac can binh thuong
    def test_checkTriangle_22(self):
        self.assertEquals(detect_triangle(2,2,3),"Tam giac can")
    def test_checkTriangle_23(self):
        self.assertEquals(detect_triangle(decimal.Decimal('10')**-9, 2**32 - 1,2**32 -1),"Tam giac can")
    def test_checkTriangle_24(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    # Kiem tra tam giac can co 2 canh cuc be
    def test_checkTriangle_25(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_26(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_27(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    # Kiem tra tam giac can co 2 canh cuc lon
    def test_checkTriangle_28(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_29(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_30(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    # Kiem tra tam giac deu
    def test_checkTriangle_31(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_32(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_33(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    # Kiem tra tam giac deu co canh vo cung be
    def test_checkTriangle_34(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_35(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_36(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    # Kiem tra tam giac vuong can
    def test_checkTriangle_37(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_38(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
    def test_checkTriangle_39(self):
        self.assertEquals(detect_triangle("",2,3),"Error")
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()