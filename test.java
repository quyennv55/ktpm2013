/* kiem thu don vi cho chuong trinh giai phong trinh bac 1 ax +b =0
*
*/
import java.io.*;
class class Test
{
	int giaiPTB1(int a, int b){
		if(a ==0) return 0;
	return -b/a;
	}
	//method test1
	static void test1(){
		int ketqua = giaiPTB1(1,1);
		if(ketqua == -1)
			System.out.prinln("Test1 was success.");
		else
			System.out.prinln("Test1 was failed.");
	}
	//method test2
	static void test2(){
		int ketqua = giaiPTB1(10,-90);
		if(ketqua == 9)
			System.out.prinln("Test2 was success.");
		else
			System.out.prinln("Test2 was failed.");
	}
	//method  test3
	void test3(){
		int ketqua = giaiPTB1(0,1);
		if(ketqua == 0)
			System.out.prinln("Test3 was success.");
		else
			System.out.prinln("Test3 was failed.");
	}

	public static void main(String[] args){
		//System.out.println("phuong trinh bac 1");
		//test1
		test1();
		//test2
		test2();
		//test3
		test3();
	}
}
