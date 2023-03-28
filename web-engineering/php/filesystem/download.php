<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    

<?php
require "vendor/autoload.php";

use Dompdf\Dompdf;

// instantiate and use the dompdf class
$dompdf = new Dompdf();


$html =  "<table>";
$html .= "<thead>";
$html .=  "<tr>";
            $html .= "<th>Title</th>";
            $html .= "<th>Dept. Name</td>";
            $html .= "<th>Credits</td>";
        $html .= "</tr>";
    $html .= "</thead>";
    $html .= "<tbody>";
        // MySQL database credentials
        $host = 'localhost';
        $username = 'root';
        $password = 'nahid1234';
        $database = 'test';

        // Create a connection
        $conn = new mysqli($host, $username, $password, $database);

        // Check if the connection was successful
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Perform a query
        $sql = "SELECT * FROM course";
        $result = $conn->query($sql);

        // Display the results
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $html .= "<tr>";

                $html .= "<td>";
                $html .= $row["title"];
                $html .= "</td>";
                $html .= "<td>";
                $html .= $row["dept_name"];
                $html .= "</td>";
                $html .= "<td>";
                $html .= $row["credits"];
                $html .= "</td>";


                $html .= "</tr>";
            }
        } else {
            echo "No results";
        }

        // Close the connection
        $conn->close();

    $html .= "</tbody>";
$html .= "</table>";

echo $html;

$dompdf->loadHtml($html);

// // (Optional) Setup the paper size and orientation
$dompdf->setPaper('A4', 'landscape');

// // Render the HTML as PDF
$dompdf->render();

// // Output the generated PDF to Browser
$dompdf->stream();
?>

</body>
</html>