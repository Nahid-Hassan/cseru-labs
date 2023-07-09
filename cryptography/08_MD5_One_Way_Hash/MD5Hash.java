import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Hash {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String input = "Hello, MD5!";
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(input.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        String md5Hash = sb.toString();
        System.out.println("Input: " + input);
        System.out.println("MD5 Hash: " + md5Hash);
    }
}
