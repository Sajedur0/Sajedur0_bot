<?php
// Telegram Bot Token (BotFather থেকে নেওয়া)
$token = getenv("BOT_TOKEN"); // অথবা সরাসরি $token = 'YOUR_BOT_TOKEN';
$website = "https://api.telegram.org/bot$token";

// ইউজারের ইনপুট গ্রহণ
$update = json_decode(file_get_contents("php://input"), true);
$message = $update['message'] ?? $update['callback_query']['message'] ?? null;

if ($message) {
    $chat_id = $message['chat']['id'];
    $first_name = $message['from']['first_name'] ?? '';
    $last_name = $message['from']['last_name'] ?? '';
    $user_name = "Hey " . $first_name . ($last_name ? " " . $last_name : "");

    // Welcome Message
    sendMessage($chat_id, $user_name . "\nWelcome to Sajedur0!");

    // Inline Keyboard Button তৈরি
    $keyboard = [
        'inline_keyboard' => [[
            ['text' => "🛠 Tools", 'callback_data' => '/tools'],
            ['text' => "💻 Code", 'callback_data' => '/code'],
            ['text' => "🌐 Website", 'url' => 'https://srr0.blogspot.com']
        ]]
    ];

    // বাটনসহ মেসেজ পাঠানো
    sendInlineKeyboard($chat_id, "⤵️ Choose an option:", $keyboard);
}

// ফাংশন: সাধারণ মেসেজ পাঠানো
function sendMessage($chat_id, $text) {
    global $website;
    file_get_contents($website . "/sendMessage?chat_id=$chat_id&text=" . urlencode($text));
}

// ফাংশন: ইনলাইন বাটনসহ মেসেজ
function sendInlineKeyboard($chat_id, $text, $keyboard) {
    global $website;
    $payload = [
        'chat_id' => $chat_id,
        'text' => $text,
        'reply_markup' => json_encode($keyboard)
    ];
    file_get_contents($website . "/sendMessage?" . http_build_query($payload));
}
?>
