Imports System

Public Module DistanceCalc
	Public Function Distance2D(From as Double(), To_ as Double()) as Double
		' Note: Here, DiffX and DiffY are already squared, instead of being 
		' squared in Delta.
		Dim DiffX as Double = Math.Pow(Math.Abs(From(0) - To_(0)), 2)
		Dim DiffY as Double = Math.Pow(Math.Abs(From(1) - To_(1)), 2)
		Dim Delta as Double = Math.Sqrt(DiffX + DiffY)
		Return Delta
	End Function
	
	Public Function Distance3D(From as Double(), To_ as Double()) as Double
		Dim From2D as Double() = {From(0), From(2)}
		Dim To2D as Double() = {To_(0), To_(2)}
		' Note: Again, the values in DiffY and DiffX are squared on declaration
		Dim DiffX as Double = Math.Pow(Distance2D(From2D, To2D), 2)
		Dim DiffY as Double = Math.Pow(Math.Abs(From(1) - To_(1)), 2)
		Dim Delta as Double = Math.Sqrt(DiffX + DiffY)
		Return Delta
	End Function
	
	Public Sub Main()
		Dim A as Double() = {1.0, 2.0, 3.0}
		Dim B as Double() = {4.0, 5.0, 6.0}
		Console.WriteLine(Distance3D(A, B))
	End Sub
End Module