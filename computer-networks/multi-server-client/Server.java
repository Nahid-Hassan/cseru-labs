// import socket library
import java.net.*;
import java.io.*;


public class Server {
    private ServerSocket serverSocket;

    public Server(ServerSocket serverSocket) {
        this.serverSocket = serverSocket;
    }

    public void StartServer() {
        try {
            while (!serverSocket.isClosed()) {
                Socket socket = serverSocket.accept();
                System.out.println("A new client connected");
            

                new Thread(new ClientHandler(socket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }       
    }

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8080);
            new Server(serverSocket).StartServer();
        } catch (IOException e) {
            e.printStackTrace();
        }
    } 
}