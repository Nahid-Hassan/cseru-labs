<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Book>
 */
class BookFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'title' => fake()->name(),
            'author' => fake()->name(),
            'isbn' => fake()->unique()->isbn13(),
            'price' =>fake()->numberBetween(100,300),
            'available' =>fake()->numberBetween(0,20)
        ];
    }
}
