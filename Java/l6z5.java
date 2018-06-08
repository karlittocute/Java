public class l6z5 {
    public static void main(String[] args) {
        int[][] arr = new int[3][5];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = (1 + (int) (Math.random() * 9));
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}//5 задание
