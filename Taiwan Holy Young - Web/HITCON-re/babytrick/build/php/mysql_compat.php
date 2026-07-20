<?php
// This challenge's src/index.php was written against PHP 5.x's classic
// mysql_* API, but the pr0ph3t/lamp base image only ships PHP 7.0 (the
// mysql extension was removed in PHP 7.0, replaced by mysqli). Rather than
// edit src/index.php (whose raw source is shown to players via the
// highlight_file(__FILE__) "source" action), bridge the gap here via
// auto_prepend_file so the challenge's own code/behavior stays untouched.
if (!function_exists('mysql_connect')) {
    $GLOBALS['__mysql_last_link'] = null;

    function mysql_connect($host, $user, $pass) {
        $link = @mysqli_connect($host, $user, $pass);
        $GLOBALS['__mysql_last_link'] = $link;
        return $link;
    }

    function mysql_select_db($dbname, $link = null) {
        $link = $link ?: $GLOBALS['__mysql_last_link'];
        return $link ? mysqli_select_db($link, $dbname) : false;
    }

    function mysql_query($query, $link = null) {
        $link = $link ?: $GLOBALS['__mysql_last_link'];
        return $link ? mysqli_query($link, $query) : false;
    }

    function mysql_fetch_object($result) {
        return $result ? mysqli_fetch_object($result) : false;
    }

    function mysql_fetch_array($result) {
        return $result ? mysqli_fetch_array($result) : false;
    }

    function mysql_num_rows($result) {
        return $result ? mysqli_num_rows($result) : false;
    }

    function mysql_close($link = null) {
        $link = $link ?: $GLOBALS['__mysql_last_link'];
        return $link ? mysqli_close($link) : false;
    }

    function mysql_error($link = null) {
        $link = $link ?: $GLOBALS['__mysql_last_link'];
        return $link ? mysqli_error($link) : mysqli_connect_error();
    }

    function mysql_escape_string($str) {
        $link = $GLOBALS['__mysql_last_link'];
        return $link ? mysqli_real_escape_string($link, $str) : addslashes($str);
    }
}
