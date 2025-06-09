using System;

// Clase que representa un círculo
public class Circulo
{
    private double radio; // Almacena el radio del círculo

    // Propiedad de solo lectura para obtener el radio
    public double Radio => radio;

    // Constructor que valida y asigna el radio
    public Circulo(double radio)
    {
        if (radio <= 0)
            throw new ArgumentException("El radio debe ser mayor que cero.");
        this.radio = radio;
    }

    // Método que calcula el área del círculo
    public double CalcularArea()
    {
        return Math.PI * radio * radio;
    }

    // Método que calcula el perímetro (circunferencia) del círculo
    public double CalcularPerimetro()
    {
        return 2 * Math.PI * radio;
    }
}

// Clase que representa un rectángulo
public class Rectangulo
{
    private double largo; // Almacena el largo
    private double ancho; // Almacena el ancho

    // Propiedades de solo lectura
    public double Largo => largo;
    public double Ancho => ancho;

    // Constructor con validación de dimensiones
    public Rectangulo(double largo, double ancho)
    {
        if (largo <= 0 || ancho <= 0)
            throw new ArgumentException("El largo y el ancho deben ser mayores que cero.");
        this.largo = largo;
        this.ancho = ancho;
    }

    // Método que calcula el área del rectángulo
    public double CalcularArea()
    {
        return largo * ancho;
    }

    // Método que calcula el perímetro del rectángulo
    public double CalcularPerimetro()
    {
        return 2 * (largo + ancho);
    }
}

// Clase principal para probar las figuras
public class Program
{
    public static void Main()
    {
        try
        {
            // Crear y usar un objeto Circulo
            Circulo miCirculo = new Circulo(5.5);
            Console.WriteLine("CÍRCULO:");
            Console.WriteLine($"Radio: {miCirculo.Radio}");
            Console.WriteLine($"Área: {miCirculo.CalcularArea():F2}");
            Console.WriteLine($"Perímetro: {miCirculo.CalcularPerimetro():F2}");

            Console.WriteLine();

            // Crear y usar un objeto Rectangulo
            Rectangulo miRectangulo = new Rectangulo(4.0, 3.0);
            Console.WriteLine("RECTÁNGULO:");
            Console.WriteLine($"Largo: {miRectangulo.Largo}, Ancho: {miRectangulo.Ancho}");
            Console.WriteLine($"Área: {miRectangulo.CalcularArea():F2}");
            Console.WriteLine($"Perímetro: {miRectangulo.CalcularPerimetro():F2}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}