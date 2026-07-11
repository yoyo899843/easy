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
    <title>BreakALLCTF</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px;
      }
    </style>
    <link href="bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
    <link rel="service" href="info.xml">
  </head>

  <body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="index.php">BreakALL CTF</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="index.php">Home</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
<?php
if ($_COOKIE['user'] != 'admin') {
?>
    <h3>BreakALL CTF</h3>
	</br>
    <h4>你不是admin帳號</h4>
<?php
} else {
?>
    <h3>歡迎 admin</h3>
    
	</br>
    <h4>BreakALLCTF{9a6OalBa6Hh4iRSKczHe}</h4>
<?php
}
?>
  </body>
</html>
