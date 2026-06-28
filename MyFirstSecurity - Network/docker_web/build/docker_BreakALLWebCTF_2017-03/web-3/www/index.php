<?php 
error_reporting(0);
session_id("BreakALLCTF{BQmpK7Ip0IOxclRg5jex}");
session_start();
?>



<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="images/favicon.ico">

    <title>Login</title>


    <link href="css/bootstrap.min.css" rel="stylesheet">


    <link href="css/signin.css" rel="stylesheet">
  </head>

  <body>

    <div class="container">

      <form class="form-signin"  method="post" action="index.php">
        <h2 align="center">BreakALL CTF</h2></br>
        <input type="text" id="inputstring" class="form-control" name="string" placeholder="請輸入字串" >
	 <button class="btn btn-lg btn-primary btn-block" type="submit">輸入</button></br>
	<div class="alert alert-warning">
	<?php 
	$string = $_POST['string'];
	echo $string."</br>"; 
	?>
	</div>
    </form>
    </div> 


    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

