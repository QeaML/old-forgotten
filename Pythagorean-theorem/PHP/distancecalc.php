<?php
function distance2d($from, $to){
    $diffX = abs($from[0] - $to[0]);
    $diffY = abs($from[1] - $to[1]);
    $delta = sqrt(pow($diffX, 2) + pow($diffY, 2));
    return $delta;
}

function distance3d($from, $to){
    $from2d = [$from[0], $from[2]];
    $to2d = [$to[0], $to[2]];
    $diffX = distance2d($from2d, $to2d);
    $diffY = abs($from[1] - $to[1]);
    $delta = sqrt(pow($diffX, 2) + pow($diffY, 2));
    return $delta;
}

$a = [1.0, 2.0, 3.0];
$b = [4.0, 5.0, 6.0];
echo distance3d($a, $b);
?>
