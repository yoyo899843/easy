<?php

include './flag.php';

$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
  case 'GETFLAG':
    echo $flag;
    break;
  case 'OPTIONS':
    header("Allow: GETFLAG,OPTIONS");
    break;
  default:
    header('HTTP/1.1 501 Not Implemented');
    echo "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">
<html><head>
<title>501 Not Implemented</title>
</head><body>
<h1>Not Implemented</h1>
<p>$method to ${_SERVER['REQUEST_URI']} not supported.<br />
</p>
</body></html>";
    break;
}
?>
