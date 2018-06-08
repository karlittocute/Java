public class l6z3 {
    public static void main(String[] args) {
        int[] arr = new int[20];
        for (int i = 0; i < 20; i++) {
            arr[i] = (1 + (int) (Math.random()*20));
            System.out.print(arr[i] + " ");

        }
        System.out.println();
        double average = 0;
        for (int i = 0; i<20; i++){
            average += arr[i];
        }
        average = average/20;
        System.out.println(average);

    }
}//3 задание