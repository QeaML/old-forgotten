using System;

// by iRRiNiS
	
public class Program
{
	public static double Distance2D(double[] From, double[] To)
	{
	    double DiffX = Math.Abs(From[0] - To[0]);
		double DiffY = Math.Abs(From[1] - To[1]);
		double Delta = Math.Sqrt(Math.Pow(DiffX, 2.0) + Math.Pow(DiffY, 2.0));
		return Delta;
	}
	
	public static double Distance3D(double[] From, double[] To)
    {
		double[] From2D = {From[0], From[2]};
		double[] To2D = {To[0], To[2]};
		double DiffX = Distance2D(From2D, To2D);
		double DiffY = Math.Abs(From[1] - To[1]);
		double Delta = Math.Sqrt(Math.Pow(DiffX, 2.0) + Math.Pow(DiffY, 2.0));
		return Delta;
	}

	public static void Main()
	{
		double[] A = {1.0, 2.0, 3.0};
		double[] B = {4.0, 5.0, 6.0};
		
		Console.WriteLine(Distance3D(A, B));
	}
}
