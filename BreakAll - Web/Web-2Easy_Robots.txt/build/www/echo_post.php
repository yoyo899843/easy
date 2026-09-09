<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset=utf-8>
    <title>page title</title>
    <style type="text/css">
body {
    background-image:url( ' https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS8Jg5bPNsf3LwhNlfdnBNR1NcHA-7l9CRWO89QNIzbKykW8CnP ' );
    }

#input {
  z-index: 2;
  position: absolute;
  width:30%;
  height:5%;
  top:35%;
  left:33%;
  border: 1px solid #FFF;
  background-color: #82FFFF;
}
#buttom {
  z-index: 2;
  position: absolute;
  width:15%;
  height:5%;
  top:50%;
  left:40%;
  border: 1px solid #FFF;

  }

#title {
    font-size:3cm;
}

.pinkblock {
  z-index: 2;
  position: absolute;
  width:30%;
  height:20%;
  top:60%;
  left:33%;
  border: 1px solid #FFF;
  background-color: #82FFFF;
}

    </style>
</head>
<body>
<h1 id="title"  align="center">SQL Injection</h1>
    <form method="POST" action="echo_post.php">
        <input id="input" type="text" name="acc" onkeyup="value=value.replace(/[^A-z0-9]/g,'')" /><br/>
        <input type="hidden" name="aa" />
        <input id="buttom" type="submit" />
    </form>

<?php
$db = new PDO('sqlite:' . __DIR__ . '/app.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_SILENT);
if(isset($_POST["aa"])){
$ID = $_POST["acc"];
//$password = $_POST["pass"];
//$ID2 = preg_replace("[1]" , '\\' ,$ID);
//$pass = preg_replace("/[\'\"]+/" , '' ,$password);
//$sql="SELECT * from user WHERE account='".$username."'&& password='".$password."'";
$sql="SELECT account from user WHERE ID='".$ID."'";
$result=$db->query($sql);
 echo "<div class='pinkblock' align='center' >";
if($result){
while($row = $result->fetch(PDO::FETCH_ASSOC)){
    echo "Account:".$row['account'];
    echo "</br>";
}
}
echo "</div>";
//echo $sql;
}
?>
</body>
</html>
