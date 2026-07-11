<?php 
show_source(__FILE__); 

include("flag.php"); 
 
if (($_POST["username"] != null) and ($_POST["password"] != null)) 
{
    $username = $_POST["username"]; 
    $password = $_POST["password"]; 
	
    if ($username == 'admin' and md5($password) == '0e342768415921451524974228454469') 
    { 
        echo $message = "登入成功!";
		echo $flag;
    }
	else
	{
		echo $message = "登入失敗!"; 
	}
}
?> 