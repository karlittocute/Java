package l6z6;

public class refactor {
        public static void main(String[] args) {
            int[] arr = new int[25];
            for (int i = 0; i < 25; i++) {
                arr[i] = (1 + (int) (Math.random() * 25));
                System.out.print(arr[i] + " ");

            }
            System.out.println("\n");
            MaxX.max(arr);
            int max = 0;
            int min = 0;
            for (int i = 1; i < 25; i++) {
                if (arr[i] > arr[max]) {
                    max = i;
                }
                if (arr[i] < arr[min]) {
                    min = i;
                }
            }
            int a = arr[max];
            arr[max] = arr[min];
            arr[min] = a;
            for (int i = 0; i < 25; i++) {
                System.out.print(arr[i] + " ");
            }

        }
    } //6 задание

