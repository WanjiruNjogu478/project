<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

function getAccessToken($consumerKey, $consumerSecret) {
    $credentials = base64_encode($consumerKey . ':' . $consumerSecret);
    $url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials";

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Basic ' . $credentials]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    
    $response = curl_exec($ch);
    
    // Check for cURL errors
    if ($response === false) {
        echo 'cURL error: ' . curl_error($ch);
    } else {
        echo "API Response: " . $response;
        // Decode the response
        $data = json_decode($response);
        if (isset($data->access_token)) {
            echo "Access Token: " . $data->access_token;
        } else {
            echo "Failed to retrieve access token. Response: " . $response;
        }
    }
    
    curl_close($ch);
}

// Example usage
$consumerKey = 'slYVhu24PL0sM0Jusyp8GTetch2eqp440Pa1YLHbGFDi4hGk'; // Replace with your actual Consumer Key
$consumerSecret = 'leHrSZV2cGvAAdaOFfRnPTZbcpNNNGA6Ed8k3GWsWeWt9jvsAeEmBrHGC1rTqE0G'; // Replace with your actual Consumer Secret

getAccessToken($consumerKey, $consumerSecret);
?>