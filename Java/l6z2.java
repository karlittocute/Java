import static java.util.Arrays.sort;
public class l6z2 {
        public static void main(String[] args) {
            int[] arr = new int[25];
            for (int i = 0; i < 25; i++) {
                arr[i] = (1 + (int) (Math.random()*25));
                System.out.print(arr[i] + " ");

            }
            System.out.println();
            sort(arr);
            for (int i =0; i < 25; i++) {
                System.out.print(arr[i] + " ");
            }

        }
}//2 задание
