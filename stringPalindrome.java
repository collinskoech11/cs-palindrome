import java.util.Scanner;

public class stringPalindrome{
    static boolean isPalindrome(String str){

        int i = 0, j = str.length() - 1;
        while (i<j){
            if (str.charAt(i) != str.charAt(j))
                return false;

            i++;
            j++;
        }

        return true;
    }
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter String to be checked : ");
        String str = sc.nextLine();
        
        if (isPalindrome(str))
            System.out.println(str+" is a palindrome");
        else
            System.out.println(str+" is not a palindrome");

        sc.close();
    }
}