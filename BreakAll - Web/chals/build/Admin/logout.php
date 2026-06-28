<?php

session_start();
$_SESSION['is_login'] = false;
unset($_SESSION['is_login']);
