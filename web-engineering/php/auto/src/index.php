<!-- 

Whole program structure

auto/
    src/
        Domain/
            ClassA.php
            ClassB.php
    index.php
-->

<?php
    use Bookstore2\Domain\ClassA;
    use Bookstore\Domain\ClassB;

    function autoLoader($className) {
        // echo $className;
        $lastSlash = strpos($className, '\\') + 1;
        $className = substr($className, $lastSlash);
        $directory = str_replace('\\', '/', $className);
        $filename = __DIR__ . '/'. $directory . '.php';

        echo $filename;

        require_once($filename);
    }
    // load
    spl_autoload_register('autoLoader');

    // create object
    $classA = new ClassA();
    echo "<br>";
    echo "<br>";
    $classB = new ClassB();
?>


<!-- 
    $ php -S localhost:3000
    Open your browser - search using "localhost:3000/src/index.php" 
 -->