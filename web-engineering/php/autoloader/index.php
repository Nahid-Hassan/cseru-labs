
<?php

    use Bookstore\Domain\Book;
    use Bookstore\Domain\Customer;

    function autoloader($className)
    {
        $lastSlash = strpos($className, '\\') + 1;
        $className = substr($className, $lastSlash);
        $directory = str_replace('\\', '/', $className);
        $filename = __DIR__ . '/src/' . $directory . '.php';
        
        // echo $filename;

        require_once($filename);
    }
    spl_autoload_register('autoloader');

    $book1 = new Book("1984", "George Orwell", 9785267006323, 12);
    $customer1 = new Customer(5, 'John', 'Doe', 'johndoe@mail.com');

    echo "<br>";
    var_dump(($book1));
    echo "<br>";
    echo "<br>";
    var_dump(($customer1));

?>
