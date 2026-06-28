<?php
    header('Location: /');

    if ($_SERVER['REQUEST_METHOD'] != 'POST') {
        exit;
    }

    session_start();
    unset($_SESSION['user']);
