<?php
/*
This file contains database configuration assuming you are running mysql using user "root" and password ""
*/

define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'login');
define('749673224216-egsb8v61o3q7ac3ed54abfek8fbqgtpa.apps.googleusercontent.com', '749673224216-egsb8v61o3q7ac3ed54abfek8fbqgtpa.apps.googleusercontent.com.apps.googleusercontent.com');
// Try connecting to the Database
$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

//Check the connection
if($conn == false){
    dir('Error: Cannot connect');
}

?>
