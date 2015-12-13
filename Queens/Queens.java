import java.util.*;
public class Queens {
   // Chris Nakovski
   // Solves the 8 queens problem and prints out all possible chessboards
   // that satisfy 8 queens being on a chessboard and not being in conflict
   public static final int[] board = new int[8]; // chess board
   
   public static void main(String[] args) {
      recurse(0);  
   }
   
   private static void recurse(int boardIndex) {
      if (boardIndex == board.length) {
         System.out.println(Arrays.toString(board));
      } else {
         for (int i = 0; i < board.length; i++) {
            board[boardIndex] = i;
            if (check(boardIndex)) {
               recurse(boardIndex + 1);
            }
         }
      }
   }
   
   private static boolean check(int boardIndex) {
      for (int i = 0; i < boardIndex; i++) {
         if (board[boardIndex] == board[i] || Math.abs(i - boardIndex) == Math.abs(board[i] - board[boardIndex])) {
            return false;
         }
      }
      return true;
   }
   
   
}