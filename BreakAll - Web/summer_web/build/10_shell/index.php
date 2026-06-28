<?php
  session_start();

  $hash = @$_SESSION['user_hash'];
  if (!$hash) {
      $hash = $_SESSION['user_hash'] = md5(rand() . $_SERVER['REMOTE_ADDR']);
  }

  @mkdir("files/$hash", 0700, true);

  function getUserFiles() {
      global $hash;
      $userFiles = [];
      foreach (glob("files/$hash/*") as $path) {
          $name = pathinfo($path, PATHINFO_BASENAME);
          $userFiles []= [
              'name' => $name,
              'path' => "/files/$hash/$name",
          ];
      }
      return $userFiles;
  }

  $page = @$_GET['page'] ?: 'home';
?>
<!DOCTYPE html>
<head>
  <title>這個網站很有問題</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
  <?php
    include 'mods/_head';
    include 'mods/_nav';
    include "mods/$page";
    include 'mods/_foot';
  ?>
</body>
