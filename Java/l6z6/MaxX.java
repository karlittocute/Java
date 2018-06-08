package l6z6;

public class MaxX {
        public static void max(int[] arr) {
            int maximum = arr[0];

            for (int i = 0; i < 25; i++) {
                if (arr[i] > maximum) {
                    maximum = arr[i];
                }
            }
            System.out.println("Максимальный элемент массива = " + maximum + "\n");
        }
    }

