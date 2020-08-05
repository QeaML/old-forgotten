// QeaML, 08.02.2020

package main

import (
	"fmt"
	"math"
)

func distance2d(from [2]float64, to [2]float64) float64 {
	var diffx = math.Abs(from[0] - to[0])
	var diffy = math.Abs(from[1] - to[1])
	var delta = math.Sqrt(math.Pow(diffx, 2.0) + math.Pow(diffy, 2.0))
	return delta
}

func distance3d(from [3]float64, to [3]float64) float64 {
	from2d := [2]float64{from[0], from[2]}
	to2d := [2]float64{to[0], to[2]}
	var diffx = distance2d(from2d, to2d)
	var diffy = math.Abs(from[1] - to[1])
	var delta = math.Sqrt(math.Pow(diffx, 2.0) + math.Pow(diffy, 2.0))
	return delta
}

func main() {
	a := [3]float64{1.0, 2.0, 3.0}
	b := [3]float64{4.0, 5.0, 6.0}
	fmt.Println(distance3d(a, b))
}