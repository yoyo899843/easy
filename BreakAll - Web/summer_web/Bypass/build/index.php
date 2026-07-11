<?php

$A = @$_GET['A'];
$B = @$_GET['B'];

highlight_file(__FILE__);
echo '<hr>';

if ($A && $B)
    if ($A != $B)
        if (strcmp($A, $B) == 0)
            if (md5($A) == md5($B))
                echo file_get_contents('/flag.txt');
            else die('ERROR: MD5(A) != MD5(B)');
        else die('ERROR: strcmp(A, B) != 0');
    else die('ERROR: A == B');
else die('ERROR: A, B should be given');
