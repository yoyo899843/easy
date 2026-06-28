<html>
<body>
<h2>Image Uploader</h2>

<?php  
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
?>
<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="filename" value="upload.jpg" />
Choose a JPEG to upload:<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form> 
<div id="viewsource"><a href="/?action=source">View sourcecode</a></div>
<? 
	if($_GET['action'] === 'source'){
		highlight_file(__FILE__);
	}
}
else{
	$file = $_FILES['uploadedfile']['tmp_name'];
	if(!isset($_POST['filename'])) echo "Without Correct Parameters";
	else if(filesize($file) > 1000) echo "File must be smaller than 1kB";
	else{
		$ext = pathinfo($_POST["filename"],PATHINFO_EXTENSION);
		$target_path = "upload/" . md5($_SERVER['REMOTE_ADDR'] . file_get_contents($file)) . "." . $ext;
		if(move_uploaded_file($file, $target_path)) echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
		else echo "Something wrong during the uploading process"; 
	}
}
?>
</body>
</html> 
