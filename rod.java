import java.util.Scanner;

public class rod {

    public static int rodCutting(int length, int[] prices) {
        int[] maxRevenue = new int[length + 1];

        for (int i = 1; i <= length; i++) {
            for (int j = 1; j <= i; j++) {
                maxRevenue[i] = Math.max(maxRevenue[i], prices[j - 1] + maxRevenue[i - j]);
            }
        }

        return maxRevenue[length];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking input for rod length
        System.out.print("Enter the length of the rod: ");
        int length = scanner.nextInt();

        // Taking input for rod prices
        int[] prices = new int[length];
        System.out.print("Enter the prices separated by space: ");
        for (int i = 0; i < length; i++) {
            prices[i] = scanner.nextInt();
        }

        int maxRevenue = rodCutting(length, prices);
        System.out.println("Maximum revenue: " + maxRevenue);
    }
}
