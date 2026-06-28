<?php

// get user input
$ip = $_GET['ip'];
$flag = 0;
if(stripos($ip, "cat") !== FALSE) die("You can't use my cat!");
if(stripos($ip, "flag") !== FALSE) die("My cat doesn't like flag!");

$res = shell_exec("dig " . $ip);
$flag = 1;

?>

<head>
<link rel="stylesheet" href="bootstrap.css" media="screen">
</head>
<body style="padding: 50px">
<center>
<div class="jumbotron">
<h1>Digger</h1><br>
<form method="get" style="width: 250px">
<input type="text" placeholder="ip.." name="ip" class="form-control"><br>
<input type="submit" class="btn btn-primary">
</form><br>

</center>
<?php
if($flag === 1) {
    echo "<hr>";
    echo "<pre>".$res."</pre>";
}
?>
</div>
</body>
