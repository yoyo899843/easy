<?php

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
        header('Location: /');
        exit;
    }
    
    $username = @$_POST['username'];
    $password = @$_POST['password'];
    
    if ($username && $password) {
        
        $db = new SQLite3('/db');
        
        $hash = md5($password);

        $row = $db->querySingle(
            "SELECT * FROM users WHERE username = '$username' AND password = '$hash'", true
        );

        if ($row == null) {
            die('<script>alert("登入失敗"); location.href = "/"</script>');
        }
        
        session_start();

        $_SESSION['user'] = $row['username'];
        header('Location: /');
    } else {
        die('<script>alert("不能空"); location.href = "/"</script>');
    }
