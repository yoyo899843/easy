
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="login/images/favicon.ico">

    <title>Login</title>

    <link href="login/css/bootstrap.min.css" rel="stylesheet">

    <link href="login/css/signin.css" rel="stylesheet">
  </head>

  <body>
<?php
header("Content-type: text/html; charset=utf-8");
setcookie("Login", "0", time() + 24 * 60 * 60);
?>
  
    <div class="container">

      <form class="form-signin"  method="post" action="admin.php">
        <h2 align="center">BreakALL CTF</h2></br>
        <input type="text" id="inputUsername" class="form-control" name="name" placeholder="Username" >
	<input type="hidden" name="file" value="password.php" />
        <input type="password" id="inputPassword" class="form-control" name="pw" placeholder="Password">
		
        <button class="btn btn-lg btn-primary btn-block" type="submit">登入</button>
	
      </form>

    </div> 



    <script src="login/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

