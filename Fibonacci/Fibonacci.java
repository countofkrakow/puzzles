import java.util.*;
// Chris Nakovski
// Finds the desired fibonacci number
public class Fibonacci {
   public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
      System.out.print("Desired fibonacci number: ");
      int n = s.nextInt();
      int first = 0;
      int second = 1;
      System.out.println();
      for (int i = 1; i < n; i++) {
         int p = second;
         second = first + second;
         first = p;
      }
      System.out.println(second);
   }
}