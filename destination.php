<!DOCTYPE html> 
<html> 
  
<head> 
    <title> 
        Passing JavaScript variables to PHP 
    </title> 
</head> 
      
<body> 
    <h1 style="color:green;"> 
        GeeksforGeeks 
    </h1> 
      
    <form method="get" name="form" action="destination.php"> 
        <input type="text" placeholder="Enter Data" name="data"> 
        <input type="submit" value="Submit" > 
    </form>


<?php 
$result = $_GET['submit']; 
echo $result; 
?> 

 
</body> 
  
</html> 