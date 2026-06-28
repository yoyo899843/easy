<!DOCTYPE html>
<head>
  <title>這個網站是裸體的</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
  <h1>這個網站是裸體的</h1>
  <?php if ($_COOKIE['secret'] === 'I am naked'): ?>
    <?= file_get_contents('/flag.txt') ?>
  <?php endif; ?>
</body>
