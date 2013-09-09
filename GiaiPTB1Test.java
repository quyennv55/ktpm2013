package com.example.foo;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link Foo}.
 *
 * @author user@example.com (John Doe)
 */
@RunWith(JUnit4.class)
public class GiaiPTB1Test{

    @Test
    public void thisAlwaysPasses() {
		//goi phuong trinh
		int ketqua = GiaiPTB1(1,1);
		//kiem tra ket qua mong doi
    }

    @Test
    @Ignore
    public void thisIsIgnored() {
    }
}