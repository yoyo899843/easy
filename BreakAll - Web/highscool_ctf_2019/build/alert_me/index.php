<head>
<title>alert me</title>
<link rel="stylesheet" href="bootstrap.css" media="screen">
</head>

<script src="hook.js"></script>

<body style="padding:60px">
<?php if(isset($_GET['link'])): ?>
<h3>Here is your link: </h3>
<a href="<?php echo $_GET["link"];?>">Link</a><br><br>
<hr>
<?php endif ?>

<form method="get" style="width:260px">

<p class="lead">Give me a link: </p>
<input type="text" name="link" class="form-control"><br>
<input type="submit" class="btn btn-primary">
</form>

<br><br><br>
<p class="lead">p.s. if you can <b>alert(1)</b>, I will give you flag!</p>
</body>
