public class FunctionExample {

    // Method to calculate the sum of two numbers
    int sum(int a, int b) {
        return a + b;
    }

    // Method to calculate the average of two numbers
    double average(int a, int b) {
        return (a + b) / 2.0; // Use 2.0 to ensure double division
    }

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;

        // Call the sum method
        int resultSum = sum(num1, num2);
        System.out.println("Sum: " + resultSum);

        // Call the average method
        double resultAverage = average(num1, num2);
        System.out.println("Average: " + resultAverage);
    }
}
