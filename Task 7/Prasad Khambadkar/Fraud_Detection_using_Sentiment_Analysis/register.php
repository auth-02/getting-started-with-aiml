<?php
require_once "config.php";

$username = $password = $confirm_password = "";
$username_err = $password_err = $confirm_password_err = "";

if ($_SERVER['REQUEST_METHOD'] == "POST"){

    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = "Username cannot be blank";
        echo "<script>alert('$username_err')</script>";
    }
    else{
        $sql = "SELECT id FROM users WHERE username = ?";
        $stmt = mysqli_prepare($conn, $sql);
        if($stmt)
        {
            mysqli_stmt_bind_param($stmt, "s", $param_username);

            // Set the value of param username
            $param_username = trim($_POST['username']);

            // Try to execute this statement
            if(mysqli_stmt_execute($stmt)){
                mysqli_stmt_store_result($stmt);
                if(mysqli_stmt_num_rows($stmt) == 1)
                {
                    $username_err = "This Email is already registered"; 
                    echo "<script>alert('$username_err')</script>";
                }
                else{
                    $username = trim($_POST['username']);
                }
            }
            else{
              echo "<script>alert('Something went wrong')</script>";
            }
        }
        else {
          echo "Error: " . mysqli_error($conn);
        }
    }
    if (isset($stmt)){
    mysqli_stmt_close($stmt);
    }


// Check for password
if(empty(trim($_POST['password']))){
    $password_err = "Password cannot be blank";
    echo "<script>alert('$password_err')</script>";
}
elseif(strlen(trim($_POST['password'])) < 5){
    $password_err = "Password cannot be less than 5 characters";
    echo "<script>alert('$password_err')</script>";
}
else{
    $password = trim($_POST['password']);
}

// Check for confirm password field
if(trim($_POST['password']) !=  trim($_POST['confirm_password'])){
    $password_err = "Passwords should match";
    echo "<script>alert('Password should match')</script>";
}


// If there were no errors, go ahead and insert into the database
if(empty($username_err) && empty($password_err) && empty($confirm_password_err))
{
    $sql = "INSERT INTO users (username, password) VALUES (?, ?)";
    $stmt = mysqli_prepare($conn, $sql);
    if ($stmt)
    {
        mysqli_stmt_bind_param($stmt, "ss", $param_username, $param_password);

        // Set these parameters
        $param_username = $username;
        $param_password = password_hash($password, PASSWORD_DEFAULT);

        // Try to execute the query
        if (mysqli_stmt_execute($stmt))
        {      
            echo "<script>alert('Registration successful!')</script>";      
           
            
        }
        else{
          echo "<script>alert('Something went wrong')</script>";
        }
    }
    mysqli_stmt_close($stmt);
}
mysqli_close($conn);
}
?>







<!DOCTYPE html>
<html>
<head>
	<title>Registration Form</title>
    <!-- include the Ionicons CSS file -->
    <link rel="icon" type="image/svg" href="logo2.svg">


      
</head>
<body>
	<div class="container">
		<h1>Register</h1>
		<form action="" method="post">
			<label for="email"><b>Email</b></label>
			<input type="email"  name="username" id="inputEmail4" placeholder="Email" required>

			<label for="psw"><b>Password</b></label>
			<input type="password"  name ="password" id="inputPassword4" placeholder="Password" required>

			<label for="psw-repeat"><b>Confirm Password</b></label>
			<input type="password" name ="confirm_password" id="inputPassword" placeholder="Confirm Password" required>
			<hr>

			<button type="submit" class="registerbtn">Register</button>
           
			
                
                
           
              
		</form>
        <div class="register-options">
            <hr>
            <span class="register-text">already-registered</span>
            <hr>
          </div>
          <button type="submit" class="already-registered" onclick="window.location.href='login.php'">Already registered?</button>


	</div>
    
</html>
<style>
body {
	background-color: #000;
	font-family: Arial, sans-serif;
}

.container {
	background-color: #fff;
	border-radius: 10px;
	box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
	margin: auto;
	margin-top: 50px;
	padding: 20px;
	max-width: 500px;
}

input[type=email], input[type=password] {
	width: 100%;
	padding: 12px 20px;
	margin: 8px 0;
	display: inline-block;
	border: 1px solid #ccc;
	box-sizing: border-box;
}

button[type=submit] {
	background-color: #ff7200;
	color: white;
	padding: 14px 20px;
	margin: 8px 0;
	border: none;
	cursor: pointer;
	width: 100%;
    border-radius: 5px;
}

button[type=submit]:hover {
	opacity: 0.8;
    
    

}

hr {
	border: 1px solid #f1f1f1;
	margin-bottom: 25px;
}
.register-options {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
}

hr {
  flex: 1;
  height: 1px;
  background-color: #d9d9d9;
  margin: 0px 10px;
}

.register-text {
  font-size: 14px;
  font-weight: 500;
  color: #b3b3b3;
  text-transform: uppercase;
}



h1 {
	text-align: center;
	color: #444;
}
.already-registered {
  background-color: #ff7200;
  border: 1px solid white;
  border-radius: 5px;
  color: #FFFFFF;
  cursor: pointer;
  font-size: 14px;
  padding: 10px;
  text-align: center;
  width: 150px;
}

.already-registered:hover {
    opacity: 0.8;
}

</style>