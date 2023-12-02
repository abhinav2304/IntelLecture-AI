<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// The name of the file where questions will be stored
$questionsFile = 'questions.txt';

// Function to call Python script and return the summary
function get_summary($scriptPath, $apiKey) {
    $command = escapeshellcmd("python3 " . $scriptPath . " " . $apiKey);
    $output = shell_exec($command);
    return $output;
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if the question is not empty
    if (!empty($_POST["question"])) {
        $question = trim($_POST["question"]);
        
        // Check if the data directory exists, if not create it
        if (!is_dir('data')) {
            mkdir('data', 0777, true);
        }

        // Define the path to the questions file
        $filepath = 'data/' . $questionsFile;

        // Append the submitted question to the file
        file_put_contents($filepath, $question . PHP_EOL, FILE_APPEND);

        
        
    // Redirect back to the form after saving the question
    }

    // Redirect back to the form after saving the question
    header("Location: index.html");
    exit;

        // Output an error message
        echo "Please submit a valid question.";
    }
