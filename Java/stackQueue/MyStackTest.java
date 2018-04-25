import static org.junit.Assert.*;

import org.junit.Test;

public class MyStackTest {

	@Test
	public void testPushPop() {
		MyStack stack = new MyStack(10);
		stack.push(10);
		stack.push(11);
		stack.push(12);
		stack.pop();
		stack.push(13);
		stack.pop();
		stack.pop();
		
		assertEquals(10, stack.pop());
	}

	@Test
	public void testIfIsFull() {
		MyStack stack = new MyStack(2);
		stack.push(1);
		stack.push(2);
		assertTrue(stack.isFull());
	}
	
	@Test
	public void testIfPeekIsWorking() {
		MyStack stack = new MyStack(1);
		stack.push(10);
		assertEquals(10, stack.peek());
	}
	
	@Test
	public void testIfIsEmpty() {
		MyStack stack = new MyStack(10);
		assertTrue(stack.isEmpty());
	}
}
