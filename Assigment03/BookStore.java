import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;
public class BookStore {
    public static void main(String[]args){
        ArrayList<String>Book=new ArrayList<>();
        Book.add("Data Structure");
        Book.add("Network Marketing");
        Book.add("Advance programming");
        Book.add("Atomic habit");
        Book.add("Honour of Legacy");
        Book.add("Encryption Data");
        Book.add("Goal of the Life");
        Book.add("Dark Knight");
        Scanner sc=new Scanner(System.in);
        System.out.print("enter the char or name of book  ");

        String search= sc.nextLine().toLowerCase();
        boolean found=false;
         Iterator<String>it=Book.iterator();
        while(it.hasNext()){
            String book=it.next().toLowerCase();
            if(book.contains(search)){
                System.out.println(book);
                found=true;
            }
            }
            if(!found){
                System.out.println("invalid context");
            }
        sc.close();
        }
}
