
 
 <?php

$destination_path = $_REQUEST["destination"] . "/"; 
$target_path = "C:\uploads" . $destination_path;
$target_path = $target_path . basename( $_FILES['uploadedfile']['name']); 

echo "User=" .          $_ENV[USER] . "<br />";
echo "Source=" .        $_FILES['uploadedfile']['name'] . "<br />"; 
echo "Destination=" .   $destination_path . "<br />"; 
echo "Target path=" .   $target_path . "<br />"; 
echo "Size=" .          $_FILES['uploadedfile']['size'] . "<br />"; 
echo "Tmp name=" .    $_FILES['uploadedfile']['tmp_name'] . "<br />"; 


if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file ".  basename( $_FILES['uploadedfile']['name']). 
    " has been uploaded";
} else{
    echo "Якась хуйня трапилася";
}
?>