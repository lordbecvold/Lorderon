<?php
	$host = "127.0.0.1";
	$user  = "homepage";
	$password = "bugu45f8DVgtR48";
	 
	try {
		$account = new PDO("mysql:host=$host;dbname=account", $user, $password);
	} catch(PDOException $e) {
		die('Lorderon is offline, Please try again later.');
	}
	 
	try {
		$player = new PDO("mysql:host=$host;dbname=player", $user, $password);
	} catch(PDOException $e) {
		die('Lorderon is offline, Please try again later.');
	}
