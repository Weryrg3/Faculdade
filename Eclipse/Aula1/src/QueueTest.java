import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.LinkedList;
import java.util.Queue;

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