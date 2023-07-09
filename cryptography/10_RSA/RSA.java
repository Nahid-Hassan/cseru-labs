import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import javax.crypto.Cipher;

public class RSA {

    public static void main(String[] args) throws Exception {
        // Generate RSA key pair
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        
        keyPairGenerator.initialize(512); // You can adjust the key size as per your requirement
        KeyPair keyPair = keyPairGenerator.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Encrypt using the public key
        String plainText = "Hello, RSA!";
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());

        // Decrypt using the private key
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);

        String decryptedText = new String(decryptedBytes);
        
        System.out.println("Original: " + plainText);
        System.out.println("Encrypted: " + new String(encryptedBytes));
        System.out.println("Decrypted: " + decryptedText);
    }
}
