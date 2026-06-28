<?php

if($_SERVER['REMOTE_ADDR'] != "127.0.0.1")
    die("Only allow IP 127.0.0.1!");

die("FLAG{ssrf_bypass_limit}");
