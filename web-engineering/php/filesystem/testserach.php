/**
 * Helper function to do a partial search for string inside array.
 *
 * @param array  $array   Array of strings.
 * @param string $keyword Keyword to search.
 *
 * @return array
 */
function array_partial_search( $array, $keyword ) {
    $found = [];

    // Loop through each item and check for a match.
    foreach ( $array as $string ) {
        // If found somewhere inside the string, add.
        if ( strpos( $string, $keyword ) !== false ) {
            $found[] = $string;
        }
    }

    return $found;
}

// Simple list of fruits.
$fruits = [ 'apple', 'grapes', 'orange', 'pineapple' ];

// Result - [ 'apple', 'grapes', 'pineapple' ];
$found = array_partial_search( $fruits, 'ap' );
