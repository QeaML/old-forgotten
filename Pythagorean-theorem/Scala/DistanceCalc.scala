import scala.math._

object DistanceCalc {
  def distance2d(from: List[Double], to: List[Double]): Double = {
    val diffX = abs(from(0) - to(0))
    val diffY = abs(from(1) - to(1))
    val delta = sqrt(pow(diffX, 2) + pow(diffY, 2))
    return delta
  }

  def distance3d(from: List[Double], to: List[Double]): Double = {
    val from2d = List(from(0), from(2))
    val to2d = List(to(0), to(2))
    val diffX = distance2d(from2d, to2d)
    val diffY = abs(from(1) - to(1))
    val delta = sqrt(pow(diffX, 2) + pow(diffY, 2))
    return delta
  }
  
  def main(args: Array[String]) = {
    val a = List(1.0, 2.0, 3.0)
    val b = List(4.0, 5.0, 6.0)
    println(distance3d(a, b))
  }
}