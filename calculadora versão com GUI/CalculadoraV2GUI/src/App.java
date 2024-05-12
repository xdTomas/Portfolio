import java.awt.event.*;
import java.awt.*;
import javax.swing.*;

public class App extends JFrame implements ActionListener {
    static JFrame f;
    static JTextField textField;
    String s0, s1, s2;

    public App() {
        s0 = s1 = s2 = "";
    }

    public static void main(String[] args) {
        f = new JFrame("Calculadora");

        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        
        App calculator = new App();

        textField = new JTextField(16);
        textField.setEditable(false);

        // Cria botoes
        JButton b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, ba, bs, bd, bm, be, beq, beq1;

        b0 = new JButton("0");
        b1 = new JButton("1");
        b2 = new JButton("2");
        b3 = new JButton("3");
        b4 = new JButton("4");
        b5 = new JButton("5");
        b6 = new JButton("6");
        b7 = new JButton("7");
        b8 = new JButton("8");
        b9 = new JButton("9");

        ba = new JButton("+");
        bs = new JButton("-");
        bd = new JButton("/");
        bm = new JButton("*");
        beq = new JButton("C");
        beq1 = new JButton("=");

        be = new JButton(".");

        JPanel p = new JPanel();

        p.add(textField);
        p.add(ba);
        p.add(b1);
        p.add(b2);
        p.add(b3);
        p.add(bs);
        p.add(b4);
        p.add(b5);
        p.add(b6);
        p.add(bm);
        p.add(b7);
        p.add(b8);
        p.add(b9);
        p.add(bd);
        p.add(be);
        p.add(b0);
        p.add(beq);
        p.add(beq1);

        p.setBackground(Color.white);

        f.add(p);
        f.setSize(500, 500);
        f.setVisible(true);

        // adiciona listeners de ações
        b0.addActionListener(calculator);
        b1.addActionListener(calculator);
        b2.addActionListener(calculator);
        b3.addActionListener(calculator);
        b4.addActionListener(calculator);
        b5.addActionListener(calculator);
        b6.addActionListener(calculator);
        b7.addActionListener(calculator);
        b8.addActionListener(calculator);
        b9.addActionListener(calculator);
        ba.addActionListener(calculator);
        bs.addActionListener(calculator);
        bd.addActionListener(calculator);
        bm.addActionListener(calculator);
        be.addActionListener(calculator);
        beq.addActionListener(calculator);
        beq1.addActionListener(calculator);
    }

    public void actionPerformed(ActionEvent e) {
        String s = e.getActionCommand();

        if (s.charAt(0) >= '0' && s.charAt(0) <= '9' || s.charAt(0) == '.') {
            if (!s1.equals(""))
                s2 = s2 + s;
            else
                s0 = s0 + s;

            textField.setText(s0 + s1 + s2);
        } else if (s.charAt(0) == 'C') {
            s0 = s1 = s2 = "";
            textField.setText(s0 + s1 + s2);

        } else if (s.charAt(0) == '=') {
            double te;

            if (s1.equals("+"))
                te = (Double.parseDouble(s0) + Double.parseDouble(s2));
            else if (s1.equals("-"))
                te = (Double.parseDouble(s0) - Double.parseDouble(s2));
            else if (s1.equals("/"))
                te = (Double.parseDouble(s0) / Double.parseDouble(s2));
            else
                te = (Double.parseDouble(s0) * Double.parseDouble(s2));

            textField.setText(s0 + s1 + s2 + "=" + te);

            s0 = Double.toString(te);
            s1 = s2 = "";

        } else {
            if (s1.equals("") || s2.equals(""))
                s1 = s;
            else {
                double te;

                if (s1.equals("+"))
                    te = (Double.parseDouble(s0) + Double.parseDouble(s2));
                else if (s1.equals("-"))
                    te = (Double.parseDouble(s0) - Double.parseDouble(s2));
                else if (s1.equals("/"))
                    te = (Double.parseDouble(s0) / Double.parseDouble(s2));
                else
                    te = (Double.parseDouble(s0) * Double.parseDouble(s2));

                s0 = Double.toString(te);
                s1 = s;
                s2 = "";
            }
            textField.setText(s0 + s1 + s2);
        }
    }
}
