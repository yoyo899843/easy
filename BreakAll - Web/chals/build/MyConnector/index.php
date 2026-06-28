<?php

// flag is here: /flag

highlight_file(__FILE__);

$host = $_GET['host'];
$user = $_GET['user'];
$pwd = $_GET['pwd'];
$database = "kaibro";
$conn = new mysqli($host, $user, $pwd);
$conn->query("SHOW DATABASES");
mysqli_close($conn);
