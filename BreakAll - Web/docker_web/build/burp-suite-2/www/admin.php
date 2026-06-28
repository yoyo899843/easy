<?php
error_reporting(0);
?>	




<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>BreakALLWeb CTF</title>


    <link href="css/bootstrap.min.css" rel="stylesheet">


    <link href="css/shop-item.css" rel="stylesheet">

    <script src="js/jquery.js"></script>
		
	<script src="js/bootstrap.min.js"></script>

<script language="javascript">

function ShowHello(){
    $('#myModal').modal('show') 
	$('#myModal').on('hidden.bs.modal', function () {
    location.href="index.php";
		})
}
</script>



</head>

<?php
header("Content-type: text/html; charset=utf-8");


setcookie("Login", "0", time() + 24 * 60 * 60);


if ($_COOKIE["Login"]== 0)
{
	echo 
	"
		<div class='modal fade' id='myModal' role='dialog'>
    <div class='modal-dialog'>
    
      <!-- Modal content-->
      <div class='modal-content'>
        <div class='modal-header'>
          <button type='button' class='close' data-dismiss='modal'>&times;</button>
          <h4 class='modal-title'><strong>登入失敗!</strong></h4>
        </div>
        <div class='modal-body'>
          <p>您無權限觀看此頁面!</p>
        </div>
        <div class='modal-footer'>
         
        </div>
      </div>
      
    </div>
  </div>
	
	";
	
}
else
{
	
	echo "
	<div class='modal fade' id='myModal' role='dialog'>
    <div class='modal-dialog'>
    
      <!-- Modal content-->
      <div class='modal-content'>
        <div class='modal-header'>
          <button type='button' class='close' data-dismiss='modal'>&times;</button>
          <h4 class='modal-title'><strong>成功登入!</strong></h4>
        </div>
        <div class='modal-body'>
          <p>BreakALLCTF{An41YF4o68wjzq4xjYK9}</p>
        </div>
        <div class='modal-footer'>
         
        </div>
      </div>
      
    </div>
  </div>
	
	";
	
	
	
}


?>


  
  <?php

				
	if($_SESSION['name'] = 'null')
	{	
		echo "<script src='js/bootstrap.min.js'></script>";
		echo "<script type='text/javascript'>ShowHello();</script>";

	return;
	}	

			
	

?>
				
				

</div>
</html>
