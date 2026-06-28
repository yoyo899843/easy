<?php 
    session_start();
    if(!isset($_SESSION['user'])) {
        header("Location: login.php");
        die("Login first!");
    }
    $flag = 0;
    if(isset($_POST['money'])) {
        if(intval($_POST['money']) <= $_SESSION['money']) {
            $_SESSION['money'] -= intval($_POST['money']);
            $flag = 1;
        }
    }
?>

<head>
<meta charset="UTF-8">
<title>KAIBRO 購物商城</title>
<script src="vue.min.js"></script>
<script src="dialog-polyfill.js"></script>
<link href="./style.css" rel="stylesheet" />
<link href="https://unpkg.com/nes.css@2.2.1/css/nes.min.css" rel="stylesheet" />
<link rel="stylesheet" media="screen" href="https://fontlibrary.org/face/press-start-2p" type="text/css"/>
</head>

<body>

<div class="container" style="padding: 60px;margin-top:130px">

<header :class="{ sticky: scrollPos > 50 }">
<div class="container">
<div class="nav-brand">
<a href="#"><h1>KAIBRO BUY</h1></a>
<p>you can buy the flag here.</p>
</div>

<div class="social-buttons">
<span class="nes-text">Hi, <?php echo $_SESSION['user']; ?>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<span class="nes-text"><a href="logout.php">Logout</a></span><br>
<span class="nes-text is-error">You have $<?php echo $_SESSION['money']; ?></span>
</div>
</div>
</header>

<br>


<section class="topic">
<section class="nes-container with-title">
<h3 class="title">Buy flag?</h3>
<form method="post">
<div class="item">
Price: <span style="position:relative;" onClick="document.getElementById('dialog-rounded').showModal();">
<input class="nes-input" type="text" name="money" value="99999999" readonly="readonly"><Br><br>
<dialog class="nes-dialog is-rounded" id="dialog-rounded">
<p class="title nes-text is-error">Error</p>
<p>You can't change the money!</p>
<menu>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button class="nes-btn is-primary">&nbsp;&nbsp;OK&nbsp;&nbsp;</button>
</menu>
</dialog>
</span>
<input class="nes-btn is-primary" type="submit" value="Buy!">
</form>
</div>
</section>
</section>

<?php

if($flag === 1) {
    echo '<section class="nes-container with-title">';
    echo "<i class='nes-icon trophy is-large'></i><span class='nes-text is-success'> FLAG{baby_money_bypass!} </span><br>";
    echo '</section>';
} else if(isset($_POST['money'])) {
    echo '<section class="nes-container with-title">';
    echo "<span class='nes-text is-error'> You don't have enough money! </span><br>";
    echo '</section>';
}

?>

</body>
</div>
