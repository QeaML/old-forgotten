! by iRRiNiS

program DistanceCalc
	implicit none
	
	real, dimension(3) :: a, b
	real :: diff_x, diff_y, delta
	
	a = (/1.0, 2.0, 3.0/)
	b = (/4.0, 5.0, 6.0/)
	print *,distance3d(a, b)
	
	contains
		real function distance2d(from, to) result(delta)
			implicit none
			
			real, dimension(2), intent(in) :: from, to
			diff_x = abs(from(1) - to(1))
			diff_y = abs(from(2) - to(2))
			
			delta = sqrt((diff_x**2)+(diff_y**2))
		end function distance2d
		
		real function distance3d(from, to) result(delta)
			implicit none
			
			real, dimension(3), intent(in) :: from, to
			real, dimension(2) :: from2d, to2d
			
			from2d = (/from(1), from(3)/)
			to2d = (/to(1), to(3)/)
			
			diff_x = distance2d(from, to)
			diff_y = abs(from(2) - to(2))
			
			delta = sqrt((diff_x**2)+(diff_y**2))
		end function distance3d
end program
