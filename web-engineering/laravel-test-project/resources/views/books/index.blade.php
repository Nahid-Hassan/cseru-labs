<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Bookstore</title>
</head>

<body>
    <div class="m-4"></div>
    <div class="container">
        <h1>Bookstore - Information</h1>
        <a href="{{ route ("books.create")}}" class="btn btn-primary mt-4">Create Book</a>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Title</th>
                    <th scope="col">Author</th>
                    <th scope="col">ISBN</th>
                    <th scope="col">Price</th>
                    <th scope="col">Availabe</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($books as $book)
                <tr>
                    <th scope="row"> {{ $book->id }} </th>
                    <td> {{ $book->title  }} </td>
                    <td> {{ $book->author  }} </td>
                    <td> {{ $book->isbn  }} </td>
                    <td> {{ $book->price  }} </td>
                    <td> {{ $book->available  }} </td>
                </tr>
                @endforeach
            </tbody>
        </table>
        
        {{ $books->links() }}
    
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
</body>

</html>
