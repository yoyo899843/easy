<html>
<head>
<title>No Password</title>
<meta charset="utf-8">
<link rel="stylesheet" href="https://bootswatch.com/4/sketchy/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
<script>
$(function() {
    $('input[name$="username"]').keyup(function(){
        $('.username').text( $(this).val() );
    });
    $('input[name$="password"]').keyup(function(){
        $('.password').text( $(this).val() );
    });

    $('.username').text( $('input[name$="username"]').val() );
    $('.password').text( $('input[name$="password"]').val() );
});
</script>
<style>
.username {
    color: red;
}

.password {
    color: red;
}

#username {
    margin-bottom: 6px;
}

#password {
    margin-bottom: 6px;
}

body {
    padding-top: 55px;
}

</style>
</head>

<body>
<br>
<div class="container">

<center><h1 class="display-3">No Password</h1></center>
<br>
<div class="jumbotron">

<form method="post">
<input type="text" name="username" class="form-control form-control-lg" placeholder="Username" id="username">
<input type="password" name="password" class="form-control form-control-lg" placeholder="Password" id="password">
<input type="submit" class="btn btn-lg btn-primary" value="Sign in">
</form>

<?php

$dbuser = 'kaibro';
$dbpass = 'superbig';
$host = 'localhost';

$conn = mysql_connect($host, $dbuser, $dbpass) or die('connection failed');
mysql_query("SET NAMES utf-8");
mysql_select_db("users");

$agent = $_SERVER['HTTP_USER_AGENT'];
if(stripos($agent, 'sqlmap') !== FALSE || stripos($agent, 'havij') !== FALSE)  {
    echo "<h1 class=\"display-3\"> Don't use SQLMAP or any tool! </h1>";
} else {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    if(isset($user) || isset($pass)) {
	    $result = @mysql_query("SELECT * FROM user WHERE (username=\"".$user."\") AND (password=\"".$pass."\")");

	    $res = @mysql_fetch_array($result);
	    if($res !== NULL && $res !== false) {
		echo '<div class="alert alert-dismissible alert-success">';
		echo '  <button type="button" class="close" data-dismiss="alert">&times;</button>';
		echo "<h2>Login successful!  Here is your flag: BreakALLCTF{7kZOJ1RioM8mPbfdfU84}</h2>";
		echo '</div>';
	    } else {
		echo '<div class="alert alert-dismissible alert-danger">';
		echo '  <button type="button" class="close" data-dismiss="alert">&times;</button>';
		echo '  <strong>Login failed!</strong>';
		echo '</div>';
	    }
    }
}
?>
<br/>
<hr class="my-4">
<h2>SELECT * FROM user WHERE ( username = "<span class='username'></span>" ) AND ( password = "<span class='password'></span>" )</h2>
<br/>
</div>
<p style="color: #c7c7c7">©kaibro.tw 2019</p>
</div>
</body>
</html>
