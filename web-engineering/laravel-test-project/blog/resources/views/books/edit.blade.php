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
        <h2 class="mt-4">Update Book</h2>

        <form action="{{ route ('books.update', ['book'=>$book]) }}" method="POST" }}>
            @csrf
            @method("PATCH")
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Title</label>
                <input type="text" name="title" value="{{ $book->title }}" class="form-control" aria-describedby="emailHelp">
                @error('title')
                    <small class="text-danger"> {{ $message }} </small>
                @enderror
            </div>

            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Author</label>
                <input type="text" name="author" value="{{ $book->author }}" class="form-control" aria-describedby="emailHelp">
                @error('author')
                    <small class="text-danger"> {{ $message }} </small>
                @enderror
            </div>

            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">ISBN</label>
                <input type="text" name="isbn" value="{{ $book->isbn }}" class="form-control" aria-describedby="emailHelp">
                @error('isbn')    
                    <small class="text-danger"> {{ $message }} </small>
                @enderror
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Price</label>
                <input type="number" name="price" value="{{ $book->price }}" class="form-control" aria-describedby="emailHelp">
                @error('price')    
                    <small class="text-danger"> {{ $message }} </small>
                @enderror
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Available</label>
                <input type="number" name="available" value="{{ $book->available }}" class="form-control" aria-describedby="emailHelp">
                @error('available')     
                    <small class="text-danger"> {{ $message }} </small>
                @enderror
            </div>

            <button type="submit" class="btn btn-primary">Update</button>
            <a href="{{ route("books.index") }}" class="btn btn-secondary">Cancel</a>
        </form>

    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
</body>

</html>
