import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SHAHash {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String input = "Hello, SHA!";
        MessageDigest sha = MessageDigest.getInstance("SHA-256");
        byte[] digest = sha.digest(input.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        String shaHash = sb.toString();
        System.out.println("Input: " + input);
        System.out.println("SHA Hash: " + shaHash);
    }
}
