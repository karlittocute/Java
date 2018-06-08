package Addition;

import javax.swing.*;

public class Add {

    public static void main(String args[]) {
        Add1 r = new Add1("Add");
        r.setVisible(true);
        r.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        r.setSize(200, 150);
        r.setResizable(false);
        r.setLocationRelativeTo(null);
    }

}

