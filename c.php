<!DOCTYPE html> 
<html> 
  
<head>
<!--<script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

$(document).ready(function(){
    $("#d").click(function(){
    alert('You clicked DEFAULT button'); 
    location.replace("https://www.w3schools.com"); 
   
    
  
  });
  $("button").click(function(){

    location.replace("test"); 
  });
  




});
 -->
 


</script>
</head>
    

    <h1 style="color:green;"> 
        GeeksforGeeks 
    </h1> 
      <!--
    <form method="get"  name="form" type="1"  > 
        <input type="text" placeholder="Enter Data" name="data"> 
        <input type="submit" id="d" value="Submit"> 
    </form>
    -->

    <form method="get" action="test"> 
        <input name="data" type="text" placeholder=" Data"> 
        <input type="submit" value="Submit"> 
    </form>




<p>
code en php
<?php 
$result = $_GET['data']; 
echo $result; 

echo('a');
?> 



</p>



<h2>This is a heading</h2>

<p>This is a paragraph.</p>
<p>This is another paragraph.</p>

<button>Click me</button>




<input type="button" id="default" value="Click Me First" /><br /><br />
<input type="button" id="myButton" value="Click Me Second" />



</body> 
  
</html> 