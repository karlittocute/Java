public class l4 {
        public static void main(String[] args) {
            int a,b,c;
            for (a = 1; a<100; a++){
                for(b = 1; b<100; b++){
                    for (c = 1; c<100; c++){
                        if ((Math.pow(a,2) + Math.pow(b,2)) == Math. pow(c,2)){
                            System.out.println("a " + a + "|" + " b " + b + "|" + " c " + c);
                        }

                    }
                }
            } // 1 задание

            double result = 1;
            for (int x = 2; x<10001; x++) {
                if ((x % 2) == 0) {
                    result -= 1/x;
                } else {
                    result += 1/x;
                }
            }
            System.out.println(result); //2 задание
        }
}
