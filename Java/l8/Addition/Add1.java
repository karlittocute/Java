package Addition;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Add1 extends JFrame {
        JButton res;
        JTextField a, b, res1;
        String result;
        eHandler handler = new eHandler();

        public Add1(String s) {
            super(s);
            setLayout(new FlowLayout());
            res = new JButton("РАСЧЕТ");
            a = new JTextField(5);
            b = new JTextField(5);
            res1 = new JTextField(5);
            add(a);
            add(b);
            add(res);
            add(res1);
            res.addActionListener(handler);
        }

        public class eHandler implements ActionListener {
            public void actionPerformed(ActionEvent e) {
                int a1 = Integer.parseInt(a.getText());
                int b1 = Integer.parseInt(b.getText());
                result = String.valueOf(a1 + b1);
                res1.setText(result);
            }
        }
    }

