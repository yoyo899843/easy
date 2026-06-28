<?php

    session_start();

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $startTime = @$_SESSION['t'];
        $answer = @$_SESSION['a'];
        unset($_SESSION['t']);
        unset($_SESSION['a']);

        if ($startTime + 5 < time()) {
            die('<script>alert("你太慢了！"); location.href = "/";</script>');
        }

        $value = @$_POST['a'];
        
        if ($value != $answer) {
            die('<script>alert("你答錯了！"); location.href = "/";</script>');
        }

        die('FLAG{your hands are so fast}');
    }

    $a = 0;
    $o = [];
    $s = explode(' ', '南無喝囉怛那哆囉夜耶 南無阿唎耶 婆盧羯帝爍缽囉耶 菩提薩埵婆耶 摩訶薩埵婆耶 摩訶迦盧尼迦耶 唵 薩皤囉罰曳 數怛那怛寫 南無 悉吉慄埵伊蒙阿唎耶 婆盧吉帝室佛囉愣馱婆 南無那囉謹墀 醯利摩訶 皤哆沙咩 薩婆阿他豆輸朋 阿逝孕 薩婆薩哆那摩婆薩哆 那摩婆伽 摩罰特豆 怛姪他 唵 阿婆盧醯 盧迦帝 迦羅帝 夷醯唎 摩訶菩提薩埵 薩婆薩婆 摩囉摩囉 摩醯摩醯唎馱孕 俱盧俱盧羯蒙 度盧度盧罰闍耶帝 摩訶罰闍耶帝 陀囉陀囉 地唎尼 室佛囉耶 遮囉遮囉 摩麼罰摩囉 穆帝隸 伊醯伊醯 室那室那 阿囉參佛囉舍利 罰沙罰參 佛囉舍耶 呼嚧呼嚧摩囉 呼嚧呼嚧醯利 娑囉娑囉 悉唎悉唎 蘇嚧蘇嚧 菩提夜菩提夜 菩馱夜菩馱夜 彌帝唎夜 那囉謹墀 地利瑟尼那 波夜摩那 娑婆訶 悉陀夜 娑婆訶 摩訶悉陀夜 娑婆訶 悉陀喻藝 室皤囉耶 娑婆訶 那囉謹墀 娑婆訶 摩囉那囉 娑婆訶 悉囉僧阿穆佉耶 娑婆訶 娑婆摩訶阿悉陀夜 娑婆訶 者吉囉阿悉陀夜 娑婆訶 波陀摩羯悉陀夜 娑婆訶 那囉謹墀皤伽囉耶 娑婆訶 摩婆利勝羯囉夜 娑婆訶 南無喝囉怛那哆囉夜耶 南無阿唎耶 婆嚧吉帝 爍皤囉夜 娑婆訶 唵 悉殿都 漫多囉 跋陀耶 娑婆訶');
    $n = rand() % 100 + 100;
    while ($n --) {
        $m = rand() % 5;
        while ($m --) {
            $o []= $s[rand() % count($s)];
        }
        $k = rand() % 1000;
        $o []= $k;
        $a += $k;
    }
    $m = rand() % 5;
    while ($m --) {
        $o []= $s[rand() % count($s)];
    }

    $o = implode('，', $o);

    $_SESSION['t'] = time();
    $_SESSION['a'] = $a;

?><!DOCTYPE html>
<head>
  <title>手速大挑戰</title>
  <meta charset="utf-8">
  <style>
    body {
      margin: 20px;
    }
    .q {
      margin: 0px;
      padding: 5px;
      border: 1px solid black;
    }
  </style>
  <script>
    setTimeout(() => {
        alert('不行，太慢了！');
        location.href = '/';
    }, 5000);
  </script>
</head>
<body>
  <h2>快，請在五秒內把下文中的所有數字加起來送出：</h2>
  <form method="post">
    <input type="number" name="a">
    <input type="submit" value="送出">
  </form>
  <br>
  <div class="q">
    <?= $o ?>。
  </div>
</body>



