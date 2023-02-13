<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Submit Book</title>
</head>

<body>
    <div class="container mt-4">
        <div class="jumbotron">
            <!--
            title
            author
            available
            pages
            isbn
             -->
            <h2 class="text-center">Enter your Book Information</h2>
            <form action="update-book.php" method="post">
                <div class="form-group">
                    <input type="text" name="title" class="form-control" id="formGroupExampleInput" placeholder="Book Title">
                </div>
                <div class="form-group">
                    <input type="text" name="author" class="form-control" id="formGroupExampleInput2" placeholder="Book Author">
                </div>
                <div class="form-group">
                    <input type="text" name="available" class="form-control" id="formGroupExampleInput3" placeholder="Is Book Available">
                </div>
                <div class="form-group">
                    <input type="text" name="pages" class="form-control" id="formGroupExampleInput4" placeholder="No. of Pages">
                </div>
                <div class="form-group">
                    <input type="text" name="isbn" class="form-control" id="formGroupExampleInput5" placeholder="ISBN Number">
                </div>
                <div class="text-center">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

</html>