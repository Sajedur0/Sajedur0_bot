<?php
$token = "YOUR_BOT_TOKEN"; // টোকেন এখানে বসাও
$website = "https://api.telegram.org/bot" . $token;

$update = file_get_contents("php://input");
$update = json_decode($update, TRUE);

$chat_id = $update["message"]["chat"]["id"];
$message = $update["message"]["text"];

if ($message == "/start") {
    sendMessage($chat_id, "👋 হ্যালো! Render থেকে চালানো PHP বট!");
} else {
    sendMessage($chat_id, "তুমি লিখেছো: " . $message);
}

function sendMessage($chat_id, $message) {
    global $website;
    file_get_contents($website."/sendMessage?chat_id=".$chat_id."&text=".urlencode($message));
}
?>
