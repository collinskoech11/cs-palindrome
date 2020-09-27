import java.util.Scanner;
public class trial {
    public static void checkPalindrome(String s){
        String reverse = new StringBuffer(s).reverse().toString();

        if (s.equals(reverse)){
            System.out.println("is a palindrome");
        }else{
            System.out.println("not a palindrome ");
        }
    }
    public static void main(String []args)
    throws java.lang.Exception{
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter String to be checked : ");
        String str = sc.nextLine();
        checkPalindrome(str);
        sc.close();
    }

}
