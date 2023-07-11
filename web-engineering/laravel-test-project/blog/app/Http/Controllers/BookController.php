<?php

namespace App\Http\Controllers;

use App\Models\Book;
use Illuminate\Http\Request;

class BookController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // $books = Book::all();
        $books = Book::paginate(10);

        return view("books.index", ["books" => $books]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view("books.create");
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
        // return $request->all();
        // dd($request->all()); 

        $request->validate(
            [
                "title" => "required|string",
                "author" => "required|string",
                "isbn" => "required",
                "price" => "required|numeric",
                "available" => "required|integer",
            ]
        );

        // dd($request->all());

        Book::create([
            'title' => $request->title,
            'author' => $request->author,
            'isbn' => $request->isbn,
            'price' => $request->price,
            'available' => $request->available
        ]);

        return redirect()->route("books.index");
    }

    /**
     * Display the specified resource.
     */
    public function show(Book $book)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Book $book)
    {
        return view('books.edit', array('book' => $book));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Book $book)
    {
        $data = $request->validate(
            [
                "title" => "required|string",
                "author" => "required|string",
                "isbn" => "required",
                "price" => "required|numeric",
                "available" => "required|integer",
            ]
        );

        $book->update($data);

        return redirect()->route("books.index")->with('Success', 'Book updated successfully');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Book $book)
    {
        $book->delete();

        return redirect()->route("books.index")->with('Success', 'Book deleted successfully');
    }
}