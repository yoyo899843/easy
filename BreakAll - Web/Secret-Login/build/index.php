<?php

// show the source code
if(isset($_GET['src'])) {
    highlight_file(__FILE__);
    echo "<hr>";
}

// include config file ($secret, $flag, ...)
include("config.php");

// get user input
$pass = $_GET['pass'];

// if user's input match the secret, it will print the flag!
if( strcmp($pass, $secret) == 0 )
    echo $flag;
?>



<head>
<link rel="stylesheet" href="bootstrap.css" media="screen">
</head>
<body style="padding: 50px">
<center>
<div class="jumbotron">
<h1>Secret Login</h1><br>
<form method="get" style="width: 250px">
<input type="text" placeholder="Secret password..." name="pass" class="form-control"><br>
<input type="submit" class="btn btn-primary">
</form><br>
<a href="?src">src</a>
</center>
</div>
</body>
