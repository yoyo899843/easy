<?php
error_reporting(0);
include("flag.php");
$url=base64_decode($_GET[url]);
if( $url=="flag.php" || $url=="download.php" || $url=="sleepingsheep.mp3" || $url=="ourfrenchcafe.mp3"){

	header ( "Content-Disposition: attachment; filename=".$url);
	echo(file_get_contents($url));
	exit;
}
else {
	echo "沒有權限!";
}
?>