<?php
session_start();
if($_SESSION['is_login'] != false)
    header("Location: /index.php");

if(isset($_POST['user']) && isset($_POST['pass'])) {
    $user = $_POST['user'];
    $pass = $_POST['pass'];
    if($user === "kaibro" && $pass === "you_can_not_get_this_pass666") {
	$_SESSION['is_login'] = true;
	header("Location: /index.php");
    } else {
	$fail = 1;
    }
}
?>
<html>
<head>
<title>Login</title>
</head>
<body style="background-image: url('bg.gif');">
<center>
<?php
if(isset($_GET['msg']))
   echo "Login first!";
?>
<form method="post" style="border-radius:10px;padding:20px;margin-top: 100px; margin-left:35%;margin-right:35%; background-color:white">
<h2>Login</h2>
<input type="text" name="user" placeholder="username"><br><br>
<input type="password" name="pass" placeholder="password"><br><br>
<input type="submit">
</form>
<a href="index.php">< back</a>
<center>
</body>
<?php
if($fail == 1) 
   echo "<hr>Wrong username or password!<br>";
?>
</html>
