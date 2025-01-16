<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    $data = "Name: $name\nEmail: $email\nMessage: $message\n\n";
    file_put_contents('submissions.txt', $data, FILE_APPEND);
    echo "Thank you for your submission!";
} else {
    echo "Invalid request method.";
}
?>
