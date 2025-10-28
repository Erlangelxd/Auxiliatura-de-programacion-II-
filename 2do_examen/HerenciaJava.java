import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Empleado p1 = new Empleado("Erlan", 20, 20000);
        p1.saludar();
        p1.trabajar();
    }
}

class Persona{
    public String nombre;
    private int edad;
    public Persona(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }
    public void setEdad(int newEdad){
        this.edad = newEdad;
    }
    public void saludar(){
        System.out.println("Hola mi nombre es " + this.nombre);
    }
}

class Empleado extends Persona{
    public int salario;
    public Empleado(String nombre, int edad, int salario){
        super(nombre, edad);
        this.salario = salario;
    }
    public void trabajar(){
        System.out.println("Trabajando");
    }
}
