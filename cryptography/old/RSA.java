import java.math.BigInteger;
import java.security.SecureRandom;

public class RSA {

  private BigInteger modulus;
  private BigInteger privateKey;
  private BigInteger publicKey;

  public RSA(int bitLength) {
    SecureRandom random = new SecureRandom();
    BigInteger p = BigInteger.probablePrime(bitLength/2, random);
    BigInteger q = BigInteger.probablePrime(bitLength/2, random);
    modulus = p.multiply(q);
    BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
    publicKey = BigInteger.probablePrime(bitLength/4, random);
    while (phi.gcd(publicKey).compareTo(BigInteger.ONE) > 0 && publicKey.compareTo(phi) < 0) {
      publicKey = publicKey.add(BigInteger.ONE);
    }
    privateKey = publicKey.modInverse(phi);
  }

  public byte[] encrypt(byte[] plaintext) {
    BigInteger message = new BigInteger(plaintext);
    BigInteger ciphertext = message.modPow(publicKey, modulus);
    return ciphertext.toByteArray();
  }

  public byte[] decrypt(byte[] ciphertext) {
    BigInteger message = new BigInteger(ciphertext);
    BigInteger plaintext = message.modPow(privateKey, modulus);
    return plaintext.toByteArray();
  }

  public static void main(String[] args) {
    RSA rsa = new RSA(1024);
    String message = "Hello, world!";
    byte[] ciphertext = rsa.encrypt(message.getBytes());
    byte[] plaintext = rsa.decrypt(ciphertext);
    System.out.println("Message: " + message);
    System.out.println("Ciphertext: " + new String(ciphertext));
    System.out.println("Plaintext: " + new String(plaintext));
  }

}
