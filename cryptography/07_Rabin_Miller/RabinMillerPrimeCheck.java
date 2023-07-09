import java.math.BigInteger;
import java.util.Random;

public class RabinMillerPrimeCheck {

    // Perform Rabin-Miller Primality Test
    public static boolean isPrime(BigInteger n, int k) {
        // Check for some base cases
        if (n.equals(BigInteger.TWO) || n.equals(BigInteger.valueOf(3))) {
            return true;
        }
        if (n.compareTo(BigInteger.TWO) < 0 || n.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            return false;
        }

        // Write n - 1 as 2^r * d
        BigInteger d = n.subtract(BigInteger.ONE);
        int r = 0;
        while (d.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            d = d.divide(BigInteger.TWO);
            r++;
        }

        // Repeat the test for k random bases
        for (int i = 0; i < k; i++) {
            BigInteger a = getRandomBase(n);
            BigInteger x = a.modPow(d, n);

            if (x.equals(BigInteger.ONE) || x.equals(n.subtract(BigInteger.ONE))) {
                continue;
            }

            boolean isComposite = true;
            for (int j = 0; j < r - 1; j++) {
                x = x.modPow(BigInteger.TWO, n);
                if (x.equals(BigInteger.ONE)) {
                    return false; // n is composite
                }
                if (x.equals(n.subtract(BigInteger.ONE))) {
                    isComposite = false;
                    break;
                }
            }

            if (isComposite) {
                return false; // n is composite
            }
        }

        return true; // n is probably prime
    }

    // Generate a random base between 2 and n-2
    public static BigInteger getRandomBase(BigInteger n) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger max = n.subtract(two);
        Random rand = new Random();
        return new BigInteger(max.bitLength(), rand).add(two);
    }

    public static void main(String[] args) {
        BigInteger n = new BigInteger("1234567890123456789012345678901234567890123456789012345678901234567890");
        int k = 10; // Number of iterations

        if (isPrime(n, k)) {
            System.out.println(n + " is probably prime.");
        } else {
            System.out.println(n + " is composite.");
        }
    }
}
