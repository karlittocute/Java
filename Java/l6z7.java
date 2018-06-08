import java.util.Scanner;

public class l6z7 {
        public static void main(String[] args) {
            String s1 = "Котик поехал на работу! ";
            String s2 = "Breaking News! ";
            String s3 = "Лапки - не оправдание.";
            Scanner sc = new Scanner (System.in);
            System.out.print("Строка s4: ");
            String s4 = sc.next();
            System.out.println("Строка s5: ");
            String s5 = sc.next();
            if (s4.equals(s5)){
                String res = s1 + " " + s2;
                System.out.println(res);
            }else{
                String res = s1+ " " + s3;
                System.out.println(res);
            }
        
        }
    }

