<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Result of Cowsay</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css">
</head>
<body>
    <section class="section">
        <div class="container">
            <h1 class="title">讓我們來看看牛都說了些啥</h1>
            <?php
                if ($_SERVER["REQUEST_METHOD"] == "POST") {
                    $dns = $_POST["dns"];
                    $output = shell_exec("cowsay " . $dns);
                    echo "<pre>$output</pre>";
                }
                else {
                    echo "<p>No string provided.</p>";
                }
            ?>
        </div>
    </section>
</body>
</html>
