﻿




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="images/favicon.ico">

    <title>BreakALL CTF</title>

 
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <link href="css/signin.css" rel="stylesheet">
  </head>

  <body>

    <div class="container">

      <form class="form-signin"  method="post" action="index.php">
        <h2 align="center">BreakALL CTF</h2>
		<h4 align="center"><a href="source.php" >查看原始碼</a></h4>
  
        <input type="text" id="inputUsername" class="form-control" name="username" placeholder="Username" >
        <input type="password" id="inputPassword" class="form-control" name="password" placeholder="Password">
		
        <button class="btn btn-lg btn-primary btn-block" type="submit">登入</button>
	
     




<?php 
include("flag.php"); 
 
if (($_POST["username"] != null) and ($_POST["password"] != null)) 
{
    $username = $_POST["username"]; 
    $password = $_POST["password"]; 
	
    if ($username == 'admin' and md5($password) == '0e342768415981441523974228454469') 
    { 
        echo $message = "<div class='alert alert-warning' align='center'><strong>登入成功!</strong></div>";
		echo $flag;
    }
	else
	{
		echo $message = "<div class='alert alert-danger' align='center'><strong>登入失敗!</strong></div>"; 
	}
}


?> 
			</form>
		</div> 
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>