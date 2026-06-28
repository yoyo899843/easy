<head>
<link rel="stylesheet" href="bootstrap.css" media="screen">
</head>
<body style="padding: 50px">
<center>
<div class="jumbotron">
<h1>URL Previewer</h1><br>
<form method="get" style="width: 250px">
<input type="text" placeholder="give me url.." name="url" class="form-control"><br>
<input type="submit" class="btn btn-primary">
</form><br>
</center>
</div>
</body>

<?php
if(isset($_GET['url'])) {
    echo "<hr>";
    echo file_get_contents($_GET['url']);
}
?>

<!-- /config.php -->
