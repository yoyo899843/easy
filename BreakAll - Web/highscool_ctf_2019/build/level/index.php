<?php

if(isset($_COOKIE['level'])) {
	if(!is_numeric($_COOKIE['level'])) {
		setcookie('level', 1);
		unset($_COOKIE['level']);
		die("Bad Hacker!");
	} else {
		$lvl = intval($_COOKIE['level']);
	}
	if(isset($_GET['nextlevel'])) {
		setcookie('level', $lvl+1);
		$lvl += 1;
	}
} else {
	setcookie('level', 1);
	$lvl = 1;
}

?>

<h1>Level <?php echo $lvl; ?></h1>
<br>
flag is in the level 1000
<br><br>
<?php if($lvl < 1000): ?>
<a href="?nextlevel">Click me to next level!</a>
<?php else: ?>
<h2>Your flag: FLAG{I_like_cookie}</h2>
<?php endif ?>
