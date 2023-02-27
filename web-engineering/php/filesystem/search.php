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
    function searchBookByTitle($books, $title)
    {
        $found = [];

        // Loop through each item and check for a match.
        foreach ($books as $book) {
            // If found somewhere inside the book, add.
            if (strpos($book["title"], $title) !== false) {
                $found[] = $book["title"];
                echo $book["title"];
            }
        }

        return $found;
    }

    // Simple list of fruits.
    $fruits = ['apple', 'grapes', 'orange', 'pineapple'];

    // Result - [ 'apple', 'grapes', 'pineapple' ];
    $found = array_partial_search($fruits, 'ap');

    ?>

    <div class="table-responsive">
        <table class="table table-striped table-condensed">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Author</td>
                    <th scope="col">Available</td>
                    <th scope="col">Pages</td>
                    <th scope="col">Isbn</td>
                </tr>
            </thead>
            <tbody>
                <?php
                $jsonFile = file_get_contents("book.json");
                $books = json_decode($jsonFile, true);

                $searchTitle = $_POST["title"];
                echo $searchTitle;

                $foundBook = searchBookByTitle($books, $searchTitle);

                if ($foundBook) {
                    echo "Book found: " . $foundBook["title"] . " by " . $foundBook["author"];
                } else {
                    echo "Book not found.";
                }


                // foreach ($books as $key => $book) {
                // echo "<tr>";
                //     foreach ($book as $b) {
                //     echo "<td>";
                //         echo $b;
                //         echo "</td>";
                //     }
                //     echo "</tr>";
                // }
                ?>
            </tbody>
        </table>

</body>

</html>