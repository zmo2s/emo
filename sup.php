<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Get Text Input Field Value in JavaScript</title>
</head>
<body>
    <input type="text" placeholder="Type something..." id="myInput">
    <button type="button" onclick="getInputValue();">Get Value</button>
    
    <script>
        function getInputValue(){
            // Selecting the input element and get its value 
            var inputVal = document.getElementById("myInput").value;
    
           
            // Displaying the value
            alert(inputVal);
        }
 </script>

    <p>
            Cette ligne a été écrite entièrement en HTML.<br />
            <?php echo "Celle-ci a été écrite entièrement en PHP."; ?>
        </p>
     
        <?php
  $mytext = $inputVal;
  echo $mytext;
?>

</body>
</html>