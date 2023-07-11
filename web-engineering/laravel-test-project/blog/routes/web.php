<?php

use App\Http\Controllers\BookController;
use Illuminate\Support\Facades\Route;

// Route::get('/', function () {
//     return view('welcome');
// });

Route::get("/books", [BookController::class, "index"])->name("books.index");
Route::post("/books", [BookController::class, "store"])->name("books.store");
Route::get("/books/create", [BookController::class, "create"])->name("books.create");
Route::get("/books/{book}/edit", [BookController::class, "edit"])->name("books.edit");
Route::patch("/books/{book}", [BookController::class, "update"])->name("books.update");
Route::delete("/books/{book}", [BookController::class, "destroy"])->name("books.destroy");