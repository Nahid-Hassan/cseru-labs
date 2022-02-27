// import java scanner
import java.util.Scanner;

// java main function
public class IPClassChecking {
    public static void main(String[] args) {
        // read string and split it into array
        Scanner input = new Scanner(System.in);

        System.out.print("Enter IP address: ");
        String ip = input.nextLine();

        if(isIPValid(ip)) {
            System.out.println("\nIP is valid");
        } else {
            System.out.println("\nIP is not valid");
            return;
        }

        String[] ipArray = ip.split("\\.");

        int ipFirstOctet = Integer.parseInt(ipArray[0]);
        String ipFirstOctetBinary = Integer.toBinaryString(ipFirstOctet);

        int lengthBinary = ipFirstOctetBinary.length();
        int missingMSBZero = 8 - lengthBinary;
        ipFirstOctetBinary = "0".repeat(missingMSBZero) + ipFirstOctetBinary;

        System.out.println("-".repeat(50));
        System.out.println("First octet in integer: " + ipFirstOctet);
        System.out.println("First octet in binary: " + ipFirstOctetBinary);

        // if first bit of octet is 0, then print class A
        System.out.println("-".repeat(50));
        if (ipFirstOctetBinary.charAt(0) == '0') {
            System.out.println("Class A");
            // exit program
            System.exit(0);
        }

        // if 2nd bit of octet is 0, then print class B
        if (ipFirstOctetBinary.charAt(1) == '0') {
            System.out.println("Class B");
            // exit program
            System.exit(0);
        }

        // if 3rd bit of octet is 0, then print class C
        if (ipFirstOctetBinary.charAt(2) == '0') {
            System.out.println("Class C");
            // exit program
            System.exit(0);
        }

        // if 4th bit of octet is 0, then print class D
        if (ipFirstOctetBinary.charAt(3) == '0') {
            System.out.println("Class D");
            // exit program
            System.exit(0);
        }

        // if 5th bit of octet is 1, then print class E
        if (ipFirstOctetBinary.charAt(4) == '1') {
            System.out.println("Class E");
            // exit program
            System.exit(0);
        }

    }
    static Boolean isIPValid(String ip) {
        String[] ipArray = ip.split("\\.");
        if (ipArray.length != 4) {
            return false;
        }
        for (String octet : ipArray) {
            int octetAsInt = Integer.parseInt(octet);
            if (octetAsInt < 0 || octetAsInt > 255) {
                return false;
            }
        }
        return true;
    }
}
