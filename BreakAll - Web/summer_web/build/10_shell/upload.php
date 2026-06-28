<?php

    if ($_SERVER['REQUEST_METHOD'] != 'POST') {
        die('invalid method');
    }
    session_start();

    $hash = @$_SESSION['user_hash'];

    if (!$hash) {
        die("no hash");
    }

    $f = $_FILES['file'];

    if ($f['error']) {
        die('上傳錯誤？');
    }

    if ($f['size'] > 4096) {
        die('檔案太大了！');
    }

    $name = md5($f['name']);
    move_uploaded_file($f['tmp_name'], "files/$hash/$name.txt");

    header('Location: /?page=files');
