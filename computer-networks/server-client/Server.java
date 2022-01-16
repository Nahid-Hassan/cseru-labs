
// import net and io
import java.net.*;
import java.io.*;

public class Server {
    public static void main(String[] args) throws Exception{

        ServerSocket serverSocket = new ServerSocket(12345);
        Socket socket = serverSocket.accept();
        System.out.println("--> Connected to " + socket.getInetAddress());
        System.out.println("--> Waiting for input...and sending 'exit' to exit");
        while(true) {
        System.out.print("--> ");
        // create data input stream and data output stream
        DataInputStream in = new DataInputStream(socket.getInputStream());
        DataOutputStream out = new DataOutputStream(socket.getOutputStream());

        // read from the client
        String msg = in.readUTF();
        if (msg.equalsIgnoreCase("exit")) {
            System.out.println("--> Exiting...");
            break;
        }
        System.out.println(msg);
        // write to the client
        // concatenate the msg with todays date
        msg = "Response from server: "+ msg + ", (" + new java.util.Date() + ")";
        out.writeUTF(msg);
        }
    }
}
