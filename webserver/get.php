<?php
$con = mysqli_connect('localhost','sensor_user','511142011');
if (!$con) {
  die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"sensor");
$sql="SELECT val FROM value WHERE id = 'ESP32_001'";
$result = mysqli_query($con,$sql);
$row = mysqli_fetch_array($result);
echo $row['val'];
mysqli_close($con);
?>
