<?php

$gg = $_POST['data'];
if (isset($gg)) {
        preg_match('/^[a-zA-Z0-9=]+$/', $gg, $m);
        system("echo $m[0] | python pickle.py");
} else {
        echo "WheRe iS yOur gg?<br>";
}
highlight_file(__FILE__);
