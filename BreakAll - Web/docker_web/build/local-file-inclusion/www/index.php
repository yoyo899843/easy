
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
          <a class="brand" href="index.php?page=index.php">BreakALL CTF</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="index.php?page=index.php">Home</a></li>
			  <li><a href="index.php?page=about.php">About</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
	

<?php include("inc/" . $_GET['page']); ?>
  </body>
</html>
