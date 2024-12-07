<?php
require 'get_access_token.php';
require 'send_money.php';

// Example usage
$consumerKey = 'YOUR_CONSUMER_KEY';
$consumerSecret = 'YOUR_CONSUMER_SECRET';
$shortcode = 'YOUR_SHORTCODE'; // Your M-Pesa shortcode
$amount = 100; // Amount to send
$phoneNumber = 'RECIPIENT_PHONE_NUMBER'; // Recipient's phone number
$callbackUrl = 'http://yourdomain.com/handle_callback.php'; // Your callback URL

// Get access token
$accessToken = getAccessToken($consumerKey, $consumerSecret);

// Send money
$response = sendMoney($accessToken, $shortcode, $amount, $phoneNumber, $callbackUrl);

// Check response
if ($response) {
    echo "Transaction response: " . print_r($response, true);
} else {
    echo "Failed to send money.";
}
?>