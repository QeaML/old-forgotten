fn distance2d(from: [f64; 2], to: [f64; 2]) -> f64 {
	let diff_x = (from[0] - to[0]).abs();
	let diff_y = (from[1] - to[1]).abs();
	let delta = (diff_x.powi(2) + diff_y.powi(2)).sqrt();
	return delta;
}

fn distance3d(from: [f64; 3], to: [f64; 3]) -> f64 {
	let from2d = [from[0], from[2]];
	let to2d = [to[0], to[2]];
	let diff_x = distance2d(from2d, to2d);
	let diff_y = (from[1] - to[1]).abs();
	let delta = (diff_x.powi(2) + diff_y.powi(2)).sqrt();
	return delta;
}

fn main() {
	let a = [1.0, 2.0, 3.0];
	let b = [4.0, 5.0, 6.0];
	println!("{}", distance3d(a, b));
}