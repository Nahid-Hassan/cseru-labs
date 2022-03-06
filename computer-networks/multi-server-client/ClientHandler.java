// import java io, util and net library
import java.io.*;
import java.util.*;
import java.net.*;

public class ClientHandler implements Runnable {
    // create a clientHandler array list public
    public static ArrayList<ClientHandler> clientHandlerArrayList = new ArrayList<ClientHandler>();
    private Socket socket;
    private BufferedReader bufferedReader;
    private PrintWriter bufferedWriter;
    private String clientUserName;

    public ClientHandler(Socket socket) {
        try {
            this.socket = socket;
            // initialize bufferedReader and bufferedWriter
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            this.clientUserName = bufferedReader.readLine();
            clientHandlerArrayList.add(this);
            broadcastMessage(clientUserName + " has joined the chat room!");
        } catch (IOException e) {
            closeEverything(socket, bufferedReader, bufferedWriter);
        }
    }

    // override run method
    @Override
    public void run() {
        String messageFromClient;

        while(socket.isConnected()) {
            try {
                messageFromClient = bufferedReader.readLine();
                broadcastMessage(clientUserName + ": " + messageFromClient);
            } catch (IOException e) {
                closeEverything(socket, bufferedReader, bufferedWriter);
                break;
            }
        }
    }

    public void broadcastMessage(String message) {
        for (ClientHandler clientHandler : clientHandlerArrayList) {
            try {
                if (!clientHandler.clientUserName.equals(clientUserName)) {
                    clientHandler.bufferedWriter.write(message + "\n");
                    clientHandler.bufferedWriter.flush();
                }
            } catch (IOException e) {
                closeEverything(socket, bufferedReader, bufferedWriter);
            }
        }
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
}
