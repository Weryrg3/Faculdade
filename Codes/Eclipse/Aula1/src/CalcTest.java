import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CalcTest {

	@Test
	public void testSum() {
		Calc calc = new Calc();
		assertEquals(4, calc.sum(3, 1));
		assertEquals(10, calc.sum(5, 5));
	}
	
	@Test
	public void testSub() {
		Calc calc = new Calc();
		
		assertEquals(7, calc.sub(10, 3));
	}
	
	@Test
	public void testDiv() {
		Calc calc = new Calc();
		
		assertEquals(2, calc.div(4, 2));
	}
	
	@Test
	public void testMult() {
		Calc calc = new Calc();
		
		assertEquals(8, calc.mult(2, 4));
	}

}
