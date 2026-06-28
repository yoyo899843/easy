<?php
session_start();

function show_admin_menu() {
    echo "<table style='background-color:white'><thead><tr><th>Admin Menu</th></tr></thead><tbody><tr><td><a href='/s3cretUrl.php'>Secret URL</a></td></tr></tbody></table>";
}

if($_SESSION['is_login'] == false)
    header("Location: /login.php?msg");
?>
<html>
<head>
<title></title>
<style>
table,
td {
    border: 1px solid #333;
}

thead,
tfoot {
    background-color: #333;
    color: #fff;
}

a {
    margin: 60px;
}

</style>
</head>
<body style="background-image: url('bg.gif')">
<center>
<?php
show_admin_menu();
?>
</center>
</body>
</html>
