import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Exercise1 {
	static Queue<Integer> queue = new LinkedList<Integer>();

	public static void main(String[] args) {
		System.out.println("===================================\n"
				+ "       Queue Operations Menu\n"
				+ "===================================\n"
				+ "1. Add items\n"
				+ "2. Delete items\n"
				+ "3. Show the number of items\n"
				+ "4. Show min and max items\n"
				+ "5. Find an item\n"
				+ "6. Print all items\n"
				+ "7. Exit\n");
				Integer n = 0;
		while(n != 7) {
			Scanner reader = new Scanner(System.in);
			System.out.println("Enter a number: ");
			n = reader.nextInt();
			if (n == 1) {
				System.out.println("Type a number:");
				Integer v = reader.nextInt();
				queue.add(v);
				System.out.println("Number add!!");
			}else if (n == 2){
				System.out.println(queue.poll());
				System.out.println("Number deleted!!\n");
			}else if (n == 3){
				System.out.println("size: " + queue.size());
			}else if (n == 4){
			
			}else if (n == 5){
				queue.toArray();
			}else if (n == 6){
				System.out.println(queue.toString());
			}
		}
		
	}

}