<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
</head>
<body>

<div class="container">
  <br><br>
  <div class="row">
    <form method="POST">
      <div class="form-group">
        <label for="exampleInputEmail1">XML here:</label>
        <textarea rows=6 class="form-control" name="xml" placeholder="<root></root>"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
  <br><br>
  <div class="row">
        <pre>
    <?php
    libxml_disable_entity_loader (false);
    $xmlfile = $_POST['xml'];
    if(stripos($xmlfile, "php") !== FALSE) die("Don' use 'php' keyword");
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
    $creds = simplexml_import_dom($dom);
    echo $creds;
    ?>
  </div>
</div>

