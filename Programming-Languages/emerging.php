<?php
//
// IF and ELSE
//
echo "IF ELSE \n";
$speed = 110;

if($speed < 60)
{
    echo "Safe driving speed";
}
elseif($speed > 60 && $speed < 100)
{
    echo "You are burning extra fuel";
}
else
{
    // when speed is greater than 100
    echo "Its dangerous";
}

//
// SWITCH
//
echo "\nSWITCH\n";
$car = "Jaguar";

switch($car)
{
    case "Audi":
        echo "Audi is amazing";
        break;
    case "Mercedes":
        echo "Mercedes is mindblowing";
        break;
    case "Jaguar":
        echo "Jaguar is the best";
        break;
    default:
        echo "$car is Ok";
}

//
// DO .. WHILE
//
echo "\nDO WHILE\n";
$a = 1;

while($a <= 10)
{
    echo "$a | ";
    $a++;   // incrementing value of a by 1
}

$a = 1;

do {
    echo "$a | ";
    $a++;   // incrementing value of a by 1
} while($a <= 10);

//
// FOR and FOREACH
//
echo "\nFOR FOREACH\n";
for($a = 0; $a <= 2; $a++)
{
    for($b = 0; $b <= 2; $b++)
    {
        echo "$b $a ";
    }
}

$array = array("Jaguar", "Audi", "Mercedes", "BMW");

foreach($array as $var)
{
    echo "$var \n";
}

//
// FUNCTION
//
echo "\nFUNCTION\n";
function add($a, $b)
{
    $sum = $a + $b;
    // returning the result
    return $sum;
}

echo "5 + 10 = " . add(5, 10) . "";

// ARRAYS
$lamborghinis = array("Urus", "Huracan", "Aventador");
?>
