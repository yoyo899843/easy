<?php

    if (!isset($_COOKIE['N5'])) {
        setcookie('N5', '8787', time() + 600);
    }

    header('Server: N4 = 55688');

?><!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Web 好簡單</title>
    <script src="main.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!--
        N1 = 9487
    -->
    <h1>Web 好簡單</h1>
    <p>請在這個網站上找到 N1-N5，flag 就是把這些數字加起來。</p>
    <p>像這樣：<span class="flag">FLAG{N1 + N2 + N3 + N4 + N5}</span></p>
    <ul>
        <li>N1 在這裡</li>
        <li>N2 在 JavaScript 裡面</li>
        <li>N3 在 CSS 裡面</li>
        <li>N4 在 server 名稱裡面</li>
        <li>N5 在 cookie 裡面</li>
    </ul>
</body>
