<?php
include("config.php");
if(isset($_POST['submit'])) {
	$xml = file_get_contents($_FILES["upfile"]['tmp_name']);
	$data = simplexml_load_string($xml,"SimpleXMLElement",LIBXML_NOENT) ;
}
highlight_file(__FILE__);
echo "<hr>";
?>


<form method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="upfile" id="fileToUpload">
    <input type="submit" value="Upload" name="submit">
</form>
