import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        char operator;
        Double num1, num2, result;

        Scanner input = new Scanner(System.in);
        System.out.println("enter first number: ");
        num1 = input.nextDouble();

        System.out.println("enter second number(!= 0): ");
        num2 = input.nextDouble();

        if (num2 == 0) {
            System.out.print("Division by 0 is not allowed");
        } else {
            System.out.println("enter operator: +, -, *, /");
            operator = input.next().charAt(0);

            switch (operator) {
                case '+':
                    result = num1 + num2;
                    System.out.println(num1 + " + " + num2 + " = " + result);
                    break;

                case '-':
                    result = num1 - num2;
                    System.out.println(num1 + " - " + num2 + " = " + result);
                    break;

                case '*':
                    result = num1 * num2;
                    System.out.println(num1 + " * " + num2 + " = " + result);
                    break;

                case '/':
                    result = num1 / num2;
                    System.out.println(num1 + " / " + num2 + " = " + result);
                    break;

                default:
                    System.out.println("invalid operator!");
                    break;

            }
        }

        input.close();
    }
}