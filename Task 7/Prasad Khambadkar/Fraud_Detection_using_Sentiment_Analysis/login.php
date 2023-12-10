<?php
//This script will handle login
session_start();

// check if the user is already logged in
if(isset($_SESSION['username']))
{
    header("location: http://127.0.0.1:5000");
    exit;
}
require_once "config.php";

$username = $password = "";
$err = "";

// if request method is post
if ($_SERVER['REQUEST_METHOD'] == "POST"){
    if(empty(trim($_POST['username'])) || empty(trim($_POST['password'])))
    {
        echo "<script>alert('Please enter username and password');</script>";
    }
    else{
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);
    }


    if(empty($err))
    {
        $sql = "SELECT id, username, password FROM users WHERE username = ?";
        $stmt = mysqli_prepare($conn, $sql);
        mysqli_stmt_bind_param($stmt, "s", $param_username);
        $param_username = $username;


        // Try to execute this statement
        if(mysqli_stmt_execute($stmt)){
            mysqli_stmt_store_result($stmt);
            if(mysqli_stmt_num_rows($stmt) == 1)
            {
                mysqli_stmt_bind_result($stmt, $id, $username, $hashed_password);
                if(mysqli_stmt_fetch($stmt))
                {
                    if(password_verify($password, $hashed_password))
                    {
                        // this means the password is corrct. Allow user to login
                        session_start();
                        $_SESSION["username"] = $username;
                        $_SESSION["id"] = $id;
                        $_SESSION["loggedin"] = true;

                        //Redirect user to welcome page
                        header("location: home.php");
                    }
                    else {
                        echo "<script>alert('Invalid password');</script>";
                    }
                }
            }
            else {
                echo "<script>alert('Email not registered');</script>";
            }
        }
        
    }
}
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login for Fraud App Detection</title>
    <link rel="stylesheet" href="style3.css">
    <link rel="icon" type="image/svg" href="logo2.svg">
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
</head>

<body>

    <div class="main">
        <div class="navbar">
            <div class="icon">
                <h2 class="logo">FD</h2>
            </div>

            <div class="menu">
                <ul>
                    
                    <li><a href="about.html">ABOUT</a></li>
                    <li><a href="service.html">SERVICE</a></li>
                    <li><a href="blog.html">BLOG</a></li>
                    <li><a href="contact.html">CONTACT</a></li>
                </ul>
            </div>

        </div> 
        <div class="content">
            <h1>Fraud Prevention <br><span>using Sentiment Analysis</span> <br></h1>
            <p class="par">A Novel approach for the detection of Clone applications
                 <br> </p>

                <button class="cn"><a href="#">JOIN US</a></button>
              <!--  <form class="login_form" action="NEXT.html" method="post" name="form" onsubmit="return validated()"> -->
               <form action="" method="post" class="login_form" name="form">
                <div class="form">
                    <h2>Login Here</h2>
                    <input type="email"  name="username" placeholder="Enter Email Here" autocomplete="off">
                    <div id="email_error">Please fill up your Email</div>
                    <input type="password" name="password"  placeholder="Enter Password Here">
                    <div id="pass_error">Please fill up your Password</div>
                  <!--   <button class="btnn"><a href="#">Login</a></button> -->
                    <button type="submit" class="btnn">Submit</button>

                    <p class="link">Don't have an account<br>
                    <a href="register.php">Sign up </a> here</a></p>
                    <p class="liw">Log in with</p>

                    <div class="icons">
                    
                    <div class="icons">
                        <a href="https://www.facebook.com"><ion-icon name="logo-facebook"></ion-icon></a>
                        <a href="https://www.instagram.com"><ion-icon name="logo-instagram"></ion-icon></a>
                        <a href="https://www.twitter.com"><ion-icon name="logo-twitter"></ion-icon></a>
                        <a href="https://www.google.com"><ion-icon name="logo-google"></ion-icon></a>
                        <a href="https://www.skype.com"><ion-icon name="logo-skype"></ion-icon></a>
                    </div>
                    </div>

                </div>
                    </div>
                </div>
        </div>
    </div>
    <script src="https://unpkg.com/ionicons@5.4.0/dist/ionicons.js"></script>
    <script>
    
</body>
</html>


