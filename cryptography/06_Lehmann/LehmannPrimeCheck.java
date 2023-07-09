import java.math.BigInteger;
import java.util.Random;

public class LehmannPrimeCheck {
    static boolean isPrime(BigInteger n, int t) {
        Random rand = new Random();
        BigInteger two = BigInteger.valueOf(2);
        BigInteger a, exponent, result;

        while (t-- > 0) {
            // a = [2, n - 1]
            a = new BigInteger(n.bitLength() - 2, rand).add(two);
            // exponent = (n - 1) / 2
            exponent = n.subtract(BigInteger.ONE).divide(two);
            // result = (a ^ exponent) % n
            result = a.modPow(exponent, n);

            if (!result.equals(BigInteger.ONE) && !result.equals(n.subtract(BigInteger.ONE))) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        BigInteger n = new BigInteger("103"); 
        int t = 10; // Number of tries

        if (n.equals(BigInteger.TWO)) {
            System.out.println("2 is Prime.");
        } else if (n.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            System.out.println(n + " is Composite.");
        } else {
            boolean isPrime = isPrime(n, t);

            if (isPrime) {
                System.out.println(n + " may be Prime.");
            } else {
                System.out.println(n + " is Composite.");
            }
        }
    }
}
