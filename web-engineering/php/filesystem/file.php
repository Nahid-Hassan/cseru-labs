<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
    <title>List of Books</title>
</head>

<body>
    <div class="container pt-4">
        <h2 class="text-center pb-2">Online Library</h2>
        <div class="text-center">
            <form action="search.php" method="post" class="form-inline">
                <div class="form-group mx-sm-3 mb-2 text-center">
                    <input type="text" class="form-control" id="inputText" placeholder="Enter the book title..." name="title">
                </div>
                <button type="submit" class="btn btn-primary mb-2">Searching...</button>
            </form>
        </div>
        <div class="p-4"></div>
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

                    foreach ($books as $key => $book) {
                        echo "<tr>";
                        foreach ($book as $b) {
                            echo "<td>";
                            echo $b;
                            echo "</td>";
                        }
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>
            <div class="text-center">
                <a class="text-center btn btn-primary" href="form.php" role="button">Add Book</a>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

</html>