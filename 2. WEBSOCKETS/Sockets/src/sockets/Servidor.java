package sockets;

import javax.swing.*;

import java.awt.*;
import java.io.DataInputStream;
import java.io.IOException;
import java.net.*;

public class Servidor  {
    public static void main(String[] args) {
        MarcoServidor mimarco=new MarcoServidor();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }	
}

class MarcoServidor extends JFrame implements Runnable{
    public MarcoServidor(){
        setBounds(1200,300,280,350);				
        JPanel milamina= new JPanel();
        milamina.setLayout(new BorderLayout());
        areatexto=new JTextArea();
        milamina.add(areatexto,BorderLayout.CENTER);
        add(milamina);
        setVisible(true);
        Thread mimhilo = new Thread(this);
        mimhilo.start();
    }
    
    @Override
    public void run() {
        try {
            ServerSocket servidor = new ServerSocket(9999);
            while(true){
                Socket miSocket = servidor.accept();
                DataInputStream flujo_entrada = new DataInputStream(miSocket.getInputStream());
                String mensaje_texto = flujo_entrada.readUTF();
                areatexto.append(mensaje_texto + "\n" );
                miSocket.close();
            }
            
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    private JTextArea areatexto;
}
