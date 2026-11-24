<?php
// Placeholders only. NOT executed.
function whats360_post(string $path, array $body, ?string $token = null): array {
    $ch = curl_init('https://whats360.live' . $path);
    $headers = ['Content-Type: application/json'];
    if ($token) $headers[] = 'Authorization: Bearer ' . $token;
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_POST => true, CURLOPT_HTTPHEADER => $headers, CURLOPT_POSTFIELDS => json_encode($body)]);
    return json_decode(curl_exec($ch), true) ?? [];
}
$token = whats360_post('/api/auth/login', ['username' => getenv('WHATS360_USER'), 'password' => getenv('WHATS360_PASSWORD')])['token'] ?? null;
print_r(whats360_post('/api/v1/email/send', ['from' => 'you@yourdomain.com', 'to' => 'recipient@example.com', 'subject' => 'Hello from API', 'body' => 'This is the email body.'], $token));
