<?php

use App\Http\Controllers\BookController;
use Illuminate\Support\Facades\Route;

// Route::get('/', function () {
//     return view('welcome');
// });

Route::get("/books", [BookController::class, "index"])->name("books.index");
Route::post("/books", [BookController::class, "store"])->name("books.store");
Route::get("/books/create", [BookController::class, "create"])->name("books.create");