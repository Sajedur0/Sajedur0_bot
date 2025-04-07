<?php
$token = getenv("BOT_TOKEN");
$website = "https://api.telegram.org/bot" . $token;

$update = file_get_contents("php://input");
$update = json_decode($update, TRUE);

$chat_id = $update["message"]["chat"]["id"] ?? null;
$message = $update["message"]["text"] ?? '';

if ($chat_id) {
    if ($message == "/start") {
        sendMessage($chat_id, "👋 হ্যালো রেন্ডার বট!");
    } else {
        sendMessage($chat_id, "তুমি লিখেছো: " . $message);
    }
}

function sendMessage($chat_id, $message) {
    global $website;
    file_get_contents($website . "/sendMessage?chat_id=" . $chat_id . "&text=" . urlencode($message));
}
?>
