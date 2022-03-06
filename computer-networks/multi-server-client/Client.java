import java.net.*;
import java.util.*;
import java.io.*;

public class Client {
    private Socket socket;
    private BufferedReader bufferedReader;
    private PrintWriter bufferedWriter;
    private String username;

    public Client(Socket socket, String username) {
        try {
            this.socket = socket;
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.username = username;
        } catch (IOException e) {
            closeEverything(socket, bufferedReader, bufferedWriter);
            e.printStackTrace();
        }
    }

    public void sendMessage() {
        try {
            bufferedWriter.write(username + '\n');
            bufferedWriter.flush();
        } catch (IOException e) {
            closeEverything(socket, bufferedReader, bufferedWriter);
        }
    }

    public void listenForMessage() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                String message;
                try {
                    while ((message = bufferedReader.readLine()) != null) {
                        System.out.println(message);
                    }
                } catch (IOException e) {
                    closeEverything(socket, bufferedReader, bufferedWriter);
                }
            }
        }).start();
    }

    public void closeEverything(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter) {
        try {
            socket.close();
            bufferedReader.close();
            bufferedWriter.close();
        } catch (IOException e) {
            System.out.println("Error closing socket, bufferedReader, or bufferedWriter");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username: ");
        String username = scanner.nextLine();
        Socket socket = new Socket("localhost", 8080);
        Client client = new Client(socket, username);
        client.listenForMessage();
        client.sendMessage();
    }
}
