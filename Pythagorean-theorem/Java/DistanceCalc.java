public class DistanceCalc {
	public static void main(String[] args){
		double[] a = {1.0, 2.0, 3.0};
		double[] b = {4.0, 5.0, 6.0};
		System.out.println(distance3d(a, b));
	}
	
	public static double distance2d(double[] from, double[] to){
		double diffX = Math.abs(from[0] - to[0]);
		double diffY = Math.abs(from[1] - to[1]);
		double delta = Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
		return delta;
	}
	
	public static double distance3d(double[] from, double[] to){
		double[] from2d = {from[0], from[2]};
		double[] to2d = {to[0], to[2]};
		double diffX = distance2d(from2d, to2d);
		double diffY = Math.abs(from[1] - to[1]);
		double delta = Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
		return delta;
	}
}