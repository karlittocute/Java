public class l6z4 {
    public static void main(String[] args) {
        int[] arr = new int[30];
        for (int i = 0; i < 30; i++) {
            arr[i] = (1 + (int) (Math.random()*30));
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        int even = 0;
        int odd = 0;
        for (int i = 0; i < 30; i++) {
            if ((arr[i]%2) == 0) {
                even = even + arr[i];
            }else{
                odd += arr[i];
            }
        }
        System.out.println(even + " " + odd);

    }
}//4 задание