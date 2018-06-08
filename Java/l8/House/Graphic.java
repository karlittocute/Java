package House;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Graphic extends JFrame {
    Graphic (String s) {
        super(s);
        setLayout(null);
        setSize(500, 500);
        setVisible(true);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setResizable(false);
        Button house = new Button("House");
        house.setBounds(5,20,100,25);
        add(house);
        house.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new House("House");
            }
        });
    }

    public static void main(String[] args) {
        new Graphic ("House");
    }
}
