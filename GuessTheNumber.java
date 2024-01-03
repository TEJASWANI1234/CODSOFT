import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int minRange = 1;
        int maxRange = 100;
        int maxAttempts = 10;
        int rounds = 0;
        int totalAttempts = 0;

        System.out.println("Welcome to Guess the Number Game!");

        // Main game loop
        while (true) {
            int secretNumber = random.nextInt(maxRange - minRange + 1) + minRange;
            int attempts = 0;
            boolean correctGuess = false;

            System.out.printf("Guess the number between %d and %d. You have %d attempts.\n", minRange, maxRange, maxAttempts);

            while (attempts < maxAttempts) {
                // Prompt the user to enter their guess
                System.out.print("Enter your guess: ");
                int userGuess = scanner.nextInt();

                // Compare the user's guess with the generated number
                if (userGuess == secretNumber) {
                    correctGuess = true;
                    break;
                } else if (userGuess < secretNumber) {
                    System.out.println("Too low! Try again.");
                } else {
                    System.out.println("Too high! Try again.");
                }

                attempts++;
            }

            // Provide feedback based on the user's guess
            if (correctGuess) {
                System.out.printf("Congratulations! You guessed the correct number %d in %d attempts.\n", secretNumber, attempts + 1);
            } else {
                System.out.printf("Sorry, you've run out of attempts. The correct number was %d.\n", secretNumber);
            }

            totalAttempts += attempts + 1;
            rounds++;

            // Ask the user if they want to play again
            System.out.print("Do you want to play again? (yes/no): ");
            String playAgain = scanner.next().toLowerCase();

            if (!playAgain.equals("yes")) {
                System.out.printf("Thanks for playing! Your average attempts per round: %.2f\n", (double) totalAttempts / rounds);
                break;
            }
        }
    }
}
