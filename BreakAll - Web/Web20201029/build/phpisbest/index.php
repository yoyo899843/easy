<html>
<body>
<h2>PHP is Best</h2>

<form action="index.php" method="POST">
<input name="name" type="text" placeholder="Enter Username" /><br />
<input name="passwd" type="password" placeholder="Enter Password"/><br />
<input type="submit" value="Login" />
</form>


<?php
require('config.php');

$_SESSION['name'] = 'user';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	// render name and passwd from POST
	extract($_POST);

	if($name === $CONFIG_NAME && $passwd === $CONFIG_PASSWD){
		$_SESSION['name'] = 'admin';
	}
	else echo "Incorrect username or password";
}
?>

<div id="viewsource"><a href="/?action=source">View sourcecode</a></div>

<?php
if($_GET['action'] === 'source')
	highlight_file(__FILE__);

if($_SESSION['name'] === 'admin')
	echo $FLAG;
?>
