import static org.junit.Assert.*;

import java.util.LinkedList;
import java.util.Queue;

import org.junit.Test;

public class QueueTest {

	@Test
	public void test() {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(1);
		queue.add(2);
		queue.add(3);
		assertEquals(new Integer(1), queue.poll());
	}

}
