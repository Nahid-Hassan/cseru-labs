import java.security.KeyPair;
import java.security.KeyPairGenerator;
import javax.crypto.KeyAgreement;
import javax.crypto.SecretKey;

public class DiffieHellman {
    public static void main(String[] args) throws Exception {
        // Generate Alice's key pair
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DH");
        keyPairGenerator.initialize(1024);
        KeyPair aliceKeyPair = keyPairGenerator.generateKeyPair();
        
        // Generate Bob's key pair
        KeyPair bobKeyPair = keyPairGenerator.generateKeyPair();
        
        // Alice performs the key agreement with Bob's public key
        KeyAgreement aliceKeyAgreement = KeyAgreement.getInstance("DH");
        aliceKeyAgreement.init(aliceKeyPair.getPrivate());
        aliceKeyAgreement.doPhase(bobKeyPair.getPublic(), true);
        
        // Bob performs the key agreement with Alice's public key
        KeyAgreement bobKeyAgreement = KeyAgreement.getInstance("DH");
        bobKeyAgreement.init(bobKeyPair.getPrivate());
        bobKeyAgreement.doPhase(aliceKeyPair.getPublic(), true);
        
        // Generate the shared secret key for Alice and Bob
        SecretKey aliceSharedSecretKey = aliceKeyAgreement.generateSecret("SunJCE");
        SecretKey bobSharedSecretKey = bobKeyAgreement.generateSecret("SunJCE");
        
        // Compare the shared secret keys to ensure they match
        boolean keysMatch = aliceSharedSecretKey.equals(bobSharedSecretKey);
        
        System.out.println("Shared Secret Keys Match: " + keysMatch);
    }
}
