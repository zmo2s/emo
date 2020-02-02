<?php
$url = '';
if(isset($_GET['url']))
{
    $url = $_GET['url'];
}
else
var_dump($_GET);


if($url == '')
    {
    include("c.php");
    }
elseif($url == "test")
{
    var_dump($_GET);
   if(isset($_GET['data']))
   {
    $data = $_GET['data'];
    echo shell_exec("sudo /var/www/html/emo/venv/bin/python3.6 /var/www/html/emo/teste15.py " . $data . " 2>&1");
   }

   
echo shell_exec("pwd");

echo('a');
}
elseif($url == "c.html?data=amour")
{


   echo shell_exec("sudo /var/www/html/emo/venv/bin/python3.6 /var/www/html/emo/teste15.py 2>&1");
echo('a');
}
else
{
echo('p');
}
    