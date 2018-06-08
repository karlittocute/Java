import java.util.Scanner;
import java.lang.Math;
public class l3 {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.print("Целое число: ");
            int n = sc.nextInt();
            int x = 2;
            for (int j=1; j<n; j++){
                x = x * 2;
            }
            System.out.println(x); //1 задание

            Scanner sc1 = new Scanner(System.in);
            System.out.println("Введите n<10: ");
            int n1 = sc1.nextInt();
            int x1;
            x1 = 1;
            for (int j=1; j<=n1; j++){
                x1 = x1*j; }
            System.out.println(x1); //2 задание

            Scanner sc2 = new Scanner(System.in);
            System.out.println("Первое число: ");
            double a = sc2.nextDouble();
            Scanner sc3 = new Scanner(System.in);
            System.out.println("Второе число: ");
            double b = sc3.nextDouble();
            System.out.println("Произведение: " + (a * b) + " Сумма: " + (a + b) + " Разность a-b: " + (a - b) + " Разность b-a: " + (b - a));  //3 задание

            Scanner sc4 = new Scanner(System.in);
            System.out.println("Высота: ");
            double h = sc4.nextDouble();
            double g=9.8;
            System.out.println(Math.sqrt((2*h/g))); //4 задание

            Scanner sc5 = new Scanner(System.in);
            System.out.println("Гипотенуза: ");
            double c = sc5.nextDouble();
            Scanner sc6 = new Scanner(System.in);
            System.out.println("Второй катет: ");
            double d = sc6.nextDouble();
            System.out.println(Math.sqrt(c * c - d * d)); //5 задание
        }
    }



