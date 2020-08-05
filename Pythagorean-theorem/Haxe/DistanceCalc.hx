class DistanceCalc{
	static function distance2d(from:Array<Float>, to:Array<Float>):Float{
		var diffX = Math.abs(from[0] - to[0]);
		var diffY = Math.abs(from[1] - to[1]);
		var delta = Math.sqrt(Math.pow(diffX, 2.0) + Math.pow(diffY, 2.0));
		return delta;
	}
	
	static function distance3d(from:Array<Float>, to:Array<Float>):Float{
		var from2d = [from[0], from[2]];
		var to2d = [to[0], to[2]];
		var diffX = distance2d(from2d, to2d);
		var diffY = Math.abs(from[1] - to[1]);
		var delta = Math.sqrt(Math.pow(diffX, 2.0) + Math.pow(diffY, 2.0));
		return delta;
	}
	
	static public function main(){
		var a = [1.0, 2.0, 3.0];
		var b = [4.0, 5.0, 6.0];
		trace(distance3d(a, b));
	}
}