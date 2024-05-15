package calculadorarmi;

import java.sql.Connection;
import java.sql.DriverManager;

public class Conectar {
    
    public Connection conexion(){
        Connection cn = null;
        
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
           
            cn = DriverManager.getConnection("jdbc:mysql://localhost:3306/calculadora", "root", "");
           
            System.out.println("Conexion establecida...");
        }catch(Exception e){
            System.out.println("ERROR: " + e);
        }
        
        return cn;
    }
}