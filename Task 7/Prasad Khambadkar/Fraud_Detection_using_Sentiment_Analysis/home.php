<?php

session_start();

if(!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !==true)
{
    header("location: login.php");
}


?>


<!DOCTYPE html>
<html>
<head>
	<title>Fraud Detection Website</title>
	<link rel="stylesheet" href="home.css">
	<link rel="icon" type="image/svg" href="logo2.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500&display=swap" rel="stylesheet">
</head>
<body>
	<div id="background"></div>
	<header>
		<h1>Fraud Detection</h1>
		<nav>
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="about.html">About Us</a></li>
				
				<li><a href="blog.html">Blog</a></li>
				<li><a href="service.html">Service</a></li>
				<li><a href="contact.html">Contact Us</a></li>
				<li><a href="logout.php">Log Out</a></li>
			</ul>
			<div class="navbar-collapse collapse">
				<ul class="navbar-nav ml-auto">
				<li class="nav-item active">
					  <a class="nav-link" href="#"> <img src="https://img.icons8.com/metro/26/000000/guest-male.png"> <?php echo "Welcome : ". $_SESSION['username']?></a>
					</li>
				</ul>
			</div>
		</nav>
	</header>
	
	<main>
		<section>
			<h2>Welcome to our Fraud Detection Website</h2>
			<p>Our platform is designed to help you identify and prevent fraudulent activities from happening. We will tell you the app you are downloading is safe or not.</p>			
		</section>
		<section>
			<h2>Review App</h2>
			<p>Have you encountered a suspicious app? We offer a review service to help you determine if it's safe to use.</p>
			<a href="http://127.0.0.1:5000">
			<button>Proceed to Review App</button>
		</a>
		</section>
        <section>
			<h2>Don't know the App ID</h2>
			<p></p>
			<a href="https://play.google.com/store/games">
			<button >Proceed to Google Play Store</button>
		</a>
		</section>		
	</main>	
</body>
</html>
