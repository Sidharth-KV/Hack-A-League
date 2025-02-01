<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>NSum</title>
        <link rel="stylesheet"
            media="screen and (orientation:landscape)"
            href="./css/l_style.css">
        <link rel="stylesheet"
            media="screen and (orientation:portrait)"
            href="./css/l_style.css">
    </head>
    <body>
        <a class="headd" href="./index.html">
            Notes Summarizer
        </a>
        <div class="box">
            <form action="upload.php"  method="post" enctype="multipart/form-data" >
                <label for="file-upload" class="custom-file-upload">
                    upload Notes (pdf,word,jpeg,png,jpg)
                </label>
                <input id="file-upload" type="file" name="userfile"/>
                <input type="submit" value="Upload">
            </form>
            <div class="message">
                <?php
                $uploadDir = "uploads/";

                $allowedTypes = ['pdf', 'docx', 'jpeg', 'jpg', 'png'];

                $maxFileSize = 20 * 1024 * 1024;

                ini_set('display_errors', 1);
                ini_set('display_startup_errors', 1);
                error_reporting(E_ALL);


                if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["userfile"])) {
                    $file = $_FILES["userfile"];
                    
                    $fileName = basename($file["name"]);
                    $fileSize = $file["size"];
                    $fileTmpName = $file["tmp_name"];
                    $fileType = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
                    $pythonScripts = [
                        'pdf'  => 'process_pdf.py',
                        'docx' => 'process_docx.py',
                        'txt'  => 'process_text.py',
                        'jpg'  => 'process_image.py',
                        'jpeg' => 'process_image.py',
                        'png'  => 'process_image.py',
                    ];
                    
                    
                    if (!in_array($fileType, $allowedTypes)) {
                        die("Error: Only PDF, DOCX, JPEG, PNG, and JPG files are allowed.");
                    }

                    if ($fileSize > $maxFileSize) {
                        die("Error: File size exceeds 5MB limit.");
                    }

                    if (!is_dir($uploadDir)) {
                        mkdir($uploadDir, 0777, true);
                    }

                    $newFileName = uniqid("upload_", true) . "." . $fileType;
                    $uploadPath = $uploadDir . $newFileName;

                    if (move_uploaded_file($fileTmpName, $uploadPath)) {
                        echo "File uploaded successfully: <a href='$uploadPath'>$fileName</a>";

                        $pythonScript = $pythonScripts[$fileType];
                        $command = escapeshellcmd("python3 scripts/$pythonScript " . escapeshellarg($fileTmpName));
                        $output = shell_exec($command);

                        echo "<pre>$output</pre>";
                    } else {
                        echo "Error: File upload failed.";
                    }
                } else {
                    echo "No file uploaded.";
                }

                ?>
            </div>
        </div>
    </body>
</html>
