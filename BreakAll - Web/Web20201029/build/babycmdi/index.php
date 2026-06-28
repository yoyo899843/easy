<html>
<body>
<h2>Baby CMDi</h2>

<form action="index.php" method="POST">
<input name="ip" type="text" placeholder="Enter IP" /><br />
<input type="submit" value="Submit" />
</form>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['ip'])) {
	$waf = array("&", "|", ";", "`", ">", "\t", "\r", "\n", "cat", "flag");
	foreach($waf as $banner){
		if(stripos($_POST['ip'], $banner) !== FALSE) die("Get Out of Here");
	}

	$result = shell_exec("ping -c 3 " . $_POST['ip']);
	echo "<pre>" . $result . "</pre>";
}
?>
