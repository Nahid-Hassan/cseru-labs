import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("localhost", 12345);
        System.out.println(">>> Connected to " + socket.getInetAddress());
        while (true) {
            System.out.print(">>> ");
            // create InputStream and OutputStream
            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());

            // write in the server
            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();
            out.writeUTF(input);
            // in.readUTF() reads the string from the server
            System.out.println(in.readUTF());
        }
    }
}
