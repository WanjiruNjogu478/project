if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $response = json_decode(file_get_contents('php://input'), true);
    // Log or process the response as needed
    file_put_contents('mpesa_response.log', print_r($response, true), FILE_APPEND);
}