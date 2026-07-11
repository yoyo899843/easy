<?php
    session_start();
    if(isset($_POST['user'])) {
        $_SESSION['user'] = $_POST['user'];
        $_SESSION['money'] = 1000;
        header("Location: index.php?msg=ok");
    }
?>

<head>
<meta charset="UTF-8">
<title>KAIBRO 購物商城</title>
<link href="https://unpkg.com/nes.css@2.2.1/css/nes.min.css" rel="stylesheet" />
<link rel="stylesheet" media="screen" href="https://fontlibrary.org/face/press-start-2p" type="text/css"/>
</head>

<body>

<div class="container" style="padding: 40px">

<br>
<section class="topic">
<section class="nes-container with-title">
<h3 class="title">Login</h3>
<form method="post">
<div class="item">
<input class="nes-input" type="text" name="user" placeholder="Username..." maxlength="8"><Br><br>
<input class="nes-btn is-primary" type="submit" value="Login!">
</div>
</form>
</section>
</section>
</body>
</div>
