<?php

namespace BookStore\Domain;

class Customer
{
  private $id;
  private $name;
  private $surname;
  private $email;
  public function __construct(
    int $id,
    string $first_name,
    string $surname,
    string $email
  ) {
    $this->id = $id;
    $this->name = $first_name;
    $this->surname = $surname;
    $this->email = $email;
  }
  public function getId(): int
  {
    return $this->id;
  }
  public function getFirstname(): string
  {
    return $this->name;
  }
  public function getSurname(): string
  {
    return $this->surname;
  }
  public function getEmail(): string
  {
    return $this->email;
  }
  public function setEmail(string $email)
  {
    $this->email = $email;
  }
}
