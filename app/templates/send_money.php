<?php
function sendMoney($accessToken, $shortcode, $amount, $phoneNumber, $callbackUrl) {
    $url = "https://api.safaricom.co.ke/mpesa/sendmoney/v1/send";

    // Prepare the data for the transaction
    $data = [
        'Initiator' => $shortcode,
        'SecurityCredential' => 'YOUR_SECURITY_CREDENTIAL', // Replace with your security credential
        'CommandID' => 'BusinessPayment',
        'Amount' => $amount,
        'PartyA' => $shortcode,
        'PartyB' => $phoneNumber,
        'Remarks' => 'Payment for services',
        'QueueTimeOutURL' => $callbackUrl,
        'ResultURL' => $callbackUrl,
    ];

    $headers = [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $accessToken,
    ];

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $response = curl_exec($ch);
    curl_close($ch);

    return json_decode($response);
}

// Example usage
$accessToken = 'YOUR_ACCESS_TOKEN'; // Get this from get_access_token.php
$shortcode = 'YOUR_SHORTCODE'; // Your M-Pesa shortcode
$amount = 100; // Amount to send
$phoneNumber = 'RECIPIENT_PHONE_NUMBER'; // Replace with the recipient's phone number
$callbackUrl = 'http://yourdomain.com/handle_callback.php'; // Your callback URL

$response = sendMoney($accessToken, $shortcode, $amount, $phoneNumber, $callbackUrl);
echo "Transaction response: " . print_r($response, true);
?>