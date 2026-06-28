<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login</title>
<meta http-equiv="Content-Type" content="text/html; charset=big5" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
</head>
<body>
 


<?php session_start(); ?>

<?php




$mysqli = new mysqli("127.0.0.1", "admin", "securitylab", "ksudb");
$name = $_POST['name'];
$pw = $_POST['pw'];
$sql = "SELECT * FROM member WHERE name = '$name' and password = '$pw'";
$result = $mysqli->query($sql);


echo "<div class='container'>";
echo "  <h2>登入訊息</h2>";

if($result->num_rows>=1)
{
$row = $result->fetch_assoc();
$rowname = $row['name'];
$rowpassword = $row['password'];


echo " <div class='panel panel-info'>";
echo "     <div class='panel-heading'>登入成功</div>";
echo "     <div class='panel-body'>帳號 : $rowname </div>";
echo "     <div class='panel-body'>密碼 : $rowpassword </div>";
echo "    </div>";

}else{

$rowname = $row['name'];
$rowpassword = $row['password'];

echo " <div class='panel panel-danger'>";
echo "     <div class='panel-heading'>登入失敗</div>";
echo "    </div>";
echo "    <meta http-equiv='refresh' content='1;url=index.php' />";
}

echo "    </div>";
echo "    </div>";
?>


 

</body>
</html>
