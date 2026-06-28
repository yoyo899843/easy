<?php

highlight_file(__FILE__);

if(!isset($_POST['payload'])) die("GIVE ME payload");
$payload = $_POST['payload'];

$b64decoded = base64_decode($payload);
if(strlen($b64decoded) > 0 ) {
	$payload = '# ' . $b64decoded;
}

if(strlen($payload) > 50) die("Too Greedy");

echo $payload;
eval($payload);

?>
