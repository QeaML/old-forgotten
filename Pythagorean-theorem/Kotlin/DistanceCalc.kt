/*
** Fun Fact!
** There's a Polish ketchup company called "Kotlin"
** QeaML, 10.02.2020
*/

fun distance2d(from: Array<Double>, to: Array<Double>): Double{
    val diffX = Math.abs(from[0] - to[0])
    val diffY = Math.abs(from[1] - to[1])
    val delta = Math.sqrt(Math.pow(diffX, 2.0) + Math.pow(diffY, 2.0))
    return delta
}

fun distance3d(from: Array<Double>, to: Array<Double>): Double{
    val from2d = Array(2){from[0]; from[2]}
    val to2d = Array(2){to[0]; to[2]}
    val diffX = distance2d(from2d, to2d)
    val diffY = Math.abs(from[1] - to[1])
    val delta = Math.sqrt(Math.pow(diffX, 2.0) + Math.pow(diffY, 2.0))
    return delta
}

fun main() {
    val a = Array(3){1.0; 2.0; 3.0}
    val b = Array(3){3.0; 4.0; 6.0}
    println(distance3d(a, b))
}