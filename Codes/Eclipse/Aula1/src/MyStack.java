
public class MyStack {

	private int maxSize;
	private long[] stack;
	private int top;
	
	public MyStack(int maxSize) {
		this.maxSize = maxSize;
		stack = new long[maxSize];
		top = -1;
	}

	public void push(int j) {
		stack[++top] = j;
	}

	public long pop() {
		return stack[top--];	
	}

	public boolean isFull() {
		
		return (top == maxSize - 1);
	}

	public long peek() {
		return stack[top];
	}

	public boolean isEmpty() {
		
		return top == -1;
	}

}