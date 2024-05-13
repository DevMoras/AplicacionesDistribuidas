package calculadorarmi;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SumadorImpl extends UnicastRemoteObject implements Sumador {
    public SumadorImpl() throws RemoteException {
        super();
    }

    public int sumar(int a, int b) throws RemoteException {
        return a + b;
    }

    public int restar(int a, int b) throws RemoteException {
        return a - b;
    }

    public int multiplicar(int a, int b) throws RemoteException {
        return a * b;
    }

    public int dividir(int a, int b) throws RemoteException {
        if (b == 0) {
            throw new RemoteException("No se puede dividir por cero.");
        }
        return a / b;
    }
}
