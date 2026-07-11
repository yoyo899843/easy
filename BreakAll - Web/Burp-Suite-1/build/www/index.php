<?php
error_reporting(E_ALL);
if (!isset($_COOKIE['user']) || empty($_COOKIE['user'])) {
  setcookie("user", "unknown");
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Login</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <link href="css/signin.css" rel="stylesheet">
    <script src="js/ie-emulation-modes-warning.js"></script>
  </head>
  <body>

    <div class="container">

      <form class="form-signin" name="form" method="post" action="member.php">
        <h2 align="center">BreakALL CTF</h2>
        <input type="text" name="name" class="form-control" placeholder="ID" >

        <input type="password" name="pw" class="form-control" placeholder="Password" >

        <button class="btn btn-lg btn-primary btn-block" type="submit">登入</button>
      </form>

    </div> 
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
