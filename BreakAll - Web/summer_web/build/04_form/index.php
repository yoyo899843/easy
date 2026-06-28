<?php
    $pw = @$_POST['pw'];
    if ($pw !== null) {
        if ($pw == '123') {
            die('FLAG{123456789}');
        } else {
            die('<script>alert("密碼錯誤！"); location.href = "/";</script>');
        }
    }
?><!DOCTYPE html>
<head>
  <title>您好！</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
  </style>
  <script>
    function checkForm(form) {
        let pw = form.querySelector('[name=pw]').value;
        if (pw == 123) {
            alert('不讓你送 123');
            return false;
        }
    }
  </script>
</head>
<body>
  <h1>打密碼就可以看 flag 喔！</h1>
  <p>偷偷告訴你，密碼是 123</p>
  <form onsubmit="return checkForm(this)" method="post">
    <input type="password" name="pw" placeholder="密碼打在這裡">
    <input type="submit" value="送出">
  </form>
</body>
