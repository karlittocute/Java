package House;

import javax.swing.*;
import java.awt.*;

public class House extends JFrame {
    House (String s){
        super (s);
        setLayout(null);
        setSize(500,500);
        setVisible(true);
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setResizable(false);
        this.setLocation(100, 100);
    }
    public void paint(Graphics gr){
        gr.setColor(Color.WHITE);
        gr.fillRect(0,0,400,400);
        gr.setColor(Color.BLACK);
        gr.drawLine(100, 400,400,400);
        gr.drawLine(400, 100,400,400);
        gr.drawLine(400, 100,100,100);
        gr.drawLine(100, 400,100,100);
        gr.drawLine(400, 100,250,30);
        gr.drawLine(100, 100,250,30);

    }
}

