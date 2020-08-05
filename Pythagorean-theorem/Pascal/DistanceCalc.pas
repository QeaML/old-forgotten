program DistanceCalc;

type
    coord2d = array[0..1] of real;
    coord3d = array[0..2] of real;

var
    a: coord3d;
    b: coord3d;
    from2d: coord2d;
    to2d: coord2d;
    diffX: real;
    diffY: real;
    delta: real;
    distance: real;

function distance2d(from: coord2d; to_: coord2d): real;
begin
    diffX := abs(from[0] - to_[0]);
    diffY := abs(from[1] - to_[1]);
    delta := sqrt((diffX * diffX) + (diffY * diffY));
    distance2d := delta;
end;

function distance3d(from: coord3d; to_: coord3d): real;
begin
    from2d[0] := from[0];
    from2d[1] := from[2];
    to2d[0] := to_[0];
    to2d[1] := to_[2];
    diffX := distance2d(from2d, to2d);
    diffY := abs(from[1] - to_[1]);
    delta := sqrt((diffX * diffX) + (diffY * diffY));
    distance3d := delta;
end;

begin
    a[0] := 1.0;
    a[1] := 2.0;
    a[2] := 3.0;
    b[0] := 4.0;
    b[1] := 5.0;
    b[2] := 6.0;
    distance := distance3d(a, b);
    writeLn(distance:1:6);
end.
