<?php

    session_start();

?><!DOCTYPE html>
<head>
  <title>登入後送你 flag</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
  <h1>登入後送你 flag</h1>
  <?php if (isset($_SESSION['user'])): ?>
    <?php if ($_SESSION['user'] != 'admin'): ?>
      嗨！你的帳號是 <?= $_SESSION['user'] ?>，要用 admin 才有 flag 啦！
    <?php else: ?>
      嗨！<?= $_SESSION['user'] ?>。給你：<pre>FLAG{the oldest database vul...}</pre>
    <?php endif; ?>
    <form action="logout.php" method="post">
      <input type="submit" value="登出">
    </form>
  <?php else: ?>
    <form action="login.php" method="post">
      <input type="text" name="username" placeholder="帳號">
      <input type="password" name="password" placeholder="密碼">
      <input type="submit" value="登入">
    </form>
  <?php endif; ?>
</body>
