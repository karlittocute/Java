import java.awt.*;
import java.applet.*;
    public class l8 extends Applet{
        public void paint(Graphics g){
            g.drawLine(100, 400,400,400);
            g.drawLine(400, 100,400,400);
            g.drawLine(400, 100,100,100);
            g.drawLine(100, 400,100,100);
            g.drawLine(400, 100,250,30);
            g.drawLine(100, 100,250,30);
        }
    }
