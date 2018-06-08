import java.applet.Applet;
import java.awt.*;
public class MyApplet extends Applet {
    public void paint (Graphics g){
        int array[][] = new int [3][3];
        for (int i = 0; i<3; i++){
            for (int j=0; j<3; j++){
                array[i][j] = (1 + (int)(Math.random()*9));
                g.drawString(Integer.toString(array[i][j]),200,150);
            }
        }
    }
}
