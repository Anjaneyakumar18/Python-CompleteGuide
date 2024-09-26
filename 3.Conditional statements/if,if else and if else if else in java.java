// IfExample.java

public class IfExample {
    public static void main(String[] args) {
        // Example of if statement
        int number = 10;
        System.out.println("Checking the number: " + number);
        if (number > 0) {
            System.out.println("The number is positive.");
        }

        System.out.println(); // Blank line for readability

        // Example of if-else statement
        int score = 75;
        System.out.println("Checking the score: " + score);
        if (score >= 60) {
            System.out.println("You passed the exam.");
        } else {
            System.out.println("You failed the exam.");
        }

        System.out.println(); // Blank line for readability

        // Example of if-else if-else statement
        int grade = 85;
        System.out.println("Checking the grade: " + grade);
        if (grade >= 90) {
            System.out.println("You got an A!");
        } else if (grade >= 80) {
            System.out.println("You got a B!");
        } else if (grade >= 70) {
            System.out.println("You got a C!");
        } else {
            System.out.println("You got a D or F.");
        }
    }
}
