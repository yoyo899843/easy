<?php
header('Content-Type:text/plain');

if (stripos($_SERVER['HTTP_USER_AGENT'],'googlebot') !== false){
	echo "User-agent: Googlebot\nAllow: /flag_2cf61812c352ec4fd0dae8f52874701d.txt";
}else{
	echo "User-agent: *\nDisallow: *";
	echo str_repeat("\n",80);
	echo "I believe that only robots like google require to know my credential page.";
}
?>
