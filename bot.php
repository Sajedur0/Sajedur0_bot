<?php

$token = getenv("BOT_TOKEN"); // Render এ সেট করা BOT_TOKEN
$website = "https://api.telegram.org/bot" . $token;

// Get update from Telegram
$update = json_decode(file_get_contents("php://input"), true);

$chat_id = $update["message"]["chat"]["id"] ?? $update["callback_query"]["message"]["chat"]["id"] ?? null;
$first_name = $update["message"]["from"]["first_name"] ?? '';
$last_name = $update["message"]["from"]["last_name"] ?? '';
$text = $update["message"]["text"] ?? '';
$data = $update["callback_query"]["data"] ?? '';

$userName = "Hey " . $first_name . ($last_name ? " " . $last_name : "");

// /start কমান্ড হ্যান্ডেল
if ($text == "/start") {
    $msg = $userName . "\nWelcome to Sajedur0!";
    sendMessage($chat_id, $msg);

    $main_buttons = [
        [
            ['text' => "🛠 Tools", 'callback_data' => "/tools"],
            ['text' => "💻 Code", 'callback_data' => "/code"],
            ['text' => "🌐 Website", 'url' => "https://srr0.blogspot.com"]
        ]
    ];

    sendInlineKeyboard($chat_id, "⤵️ Choose an option:", $main_buttons);
}

// /getfile কমান্ড হ্যান্ডেল
if (strpos($text, "/getfile") === 0) {
    $params = explode(" ", $text);
    $fileNumber = $params[1] ?? null;

    if ($fileNumber) {
        $fileUrl = "https://t.me/Sajedur0Server/" . $fileNumber . "?single";
        sendDocument($chat_id, $fileUrl, "📂 **File $fileNumber**\nStay with @Sajedur0");

        $file_buttons = [];

        for ($i = 2; $i <= 30; $i++) {
            $file_buttons[] = [['text' => "$i - File", 'callback_data' => "/getfile $i"]];
        }

        sendInlineKeyboard($chat_id, "📂 **Select a file:**", $file_buttons);
    }
}

// ফাংশন: মেসেজ পাঠানো
function sendMessage($chat_id, $text) {
    global $website;
    $url = $website . "/sendMessage?chat_id=$chat_id&text=" . urlencode($text);
    file_get_contents($url);
}

// ফাংশন: ইনলাইন বাটন সহ মেসেজ
function sendInlineKeyboard($chat_id, $text, $buttons) {
    global $website;
    $replyMarkup = json_encode(['inline_keyboard' => $buttons]);
    $post = [
        'chat_id' => $chat_id,
        'text' => $text,
        'reply_markup' => $replyMarkup,
        'parse_mode' => 'Markdown'
    ];
    sendPost($website . "/sendMessage", $post);
}

// ফাংশন: ডকুমেন্ট পাঠানো
function sendDocument($chat_id, $docUrl, $caption) {
    global $website;
    $post = [
        'chat_id' => $chat_id,
        'document' => $docUrl,
        'caption' => $caption,
        'parse_mode' => 'Markdown'
    ];
    sendPost($website . "/sendDocument", $post);
}

// ফাংশন: POST রিকুয়েস্ট
function sendPost($url, $data) {
    $options = [
        "http" => [
            "header" => "Content-Type: application/x-www-form-urlencoded\r\n",
            "method" => "POST",
            "content" => http_build_query($data)
        ]
    ];
    $context = stream_context_create($options);
    file_get_contents($url, false, $context);
}
