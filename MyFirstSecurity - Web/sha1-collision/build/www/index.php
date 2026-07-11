<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">

    <title>MyFirst CTF</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="login/css/bootstrap.min.css" rel="stylesheet">
	<link href="login/css/bootstrap.min.css" rel="stylesheet">
	<link href="css/login.css" rel="stylesheet">
    <script src="login/js/jquery-1.11.1.min.js"></script>
    <script src="login/js/bootstrap.min.js"></script>
</head>
<body>



<h2></h2>

    <div class="container">
	
        <div class="card card-container">
			<h2 class="text-center"><font color="black" >MyFirst CTF</font></h2>
			<h4 align="center"><a href="source.php" >查看原始碼</a></h4>
            <p id="profile-name" class="profile-name-card"></p>
            <form method="post" class="form-signin" action="index.php">
        
                <input type="text" id="inpuID" name="username" class="form-control" placeholder="User" >
			
                <input type="password" id="inputPassword" name="password" class="form-control" placeholder="Password" >
			
                <button class="btn btn-lg btn-success btn-block btn-signin" type="submit">登入</button>
				
				<?php 
				include("flag.php"); 
			
				 
				if (($_POST["username"] != null) and ($_POST["password"] != null)) 
				{
					$username = $_POST["username"]; 
					$password = $_POST["password"]; 
					
					if ($username == 'admin' and sha1($password) == '0e342768415931451224984248454864') 
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
    </div>
	
<script type="text/javascript">

</script>
</body>
</html>
