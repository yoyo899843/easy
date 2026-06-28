<?php
    $path = @$_GET['path'];
    if ($path) {
      $o = shell_exec("ls $path 2>&1");
    }
?><!DOCTYPE html>
<head>
  <title>您好！</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
    .o {
      margin: 0px;
      margin-top: 10px;
      padding: 5px;
      border: 1px soliod black;
    }
  </style>
</head>
<body>
  <h1>列出你想看的資料夾內容</h1>
  <form>
    <input autofocus type="text" name="path" placeholder="例如 ." value="<?= htmlentities($path) ?>">
    <input type="submit" value="送出">
  </form>
  <?php if (isset($o)): ?>
    <pre class="o"><?= htmlentities($o) ?></pre>
  <?php endif; ?>
</body>
