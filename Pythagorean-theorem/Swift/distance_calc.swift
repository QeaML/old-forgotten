func distance2d(from: [Double], to: [Double]) -> Double {
  let diffX = abs(from[0] - to[0])
  let diffY = abs(from[1] - to[1])
  let delta = ((diffX * diffX )+(diffY * diffY)).squareRoot()
  return delta
}

func distance3d(from: [Double], to: [Double]) -> Double {
  let from2d = [from[0], from[2]]
  let to2d = [to[0], to[2]]
  let diffX = distance2d(from: from2d, to: to2d)
  let diffY = abs(from[1] - to[1])
  let delta = ((diffX * diffX )+(diffY * diffY)).squareRoot()
  return delta
}

let a = [1.0, 2.0, 3.0]
let b = [4.0, 5.0, 6.0]
print(distance3d(from: a, to: b))