  <h1>0x02-python-import_modules</h1>
  <h2>Files</h2>
  <h3>0. Squared simple</h3>
  <ul>
    <li><a href="./0-square_matrix_simple.py">0-square_matrix_simple.py</a>: Python function that computes the square value of all integers of a matrix.</li>
    <li>The parameter <code>matrix</code> is a two-dimensional array.</li>
    <li>Returns a matrix of the same size as <code>matrix</code> where each value is the square of the input value.</li>
    <li>The initial matrix is not modified.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>1. Search and replace</h3>
  <ul>
    <li><a href="./1-search_replace.py">1-search_replace.py</a>: Python function that replaces all occurrences of an element with another element in a new list.</li>
    <li>The parameter <code>my_list</code> is the initial list.</li>
    <li>The parameter <code>search</code> is the element to replace in the list.</li>
    <li>The parameter <code>replace</code> is the new element.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>2. Unique addition</h3>
  <ul>
    <li><a href="./2-uniq_add.py">2-uniq_add.py</a>: Python function that adds all unique integers in a list (once for each integer).</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>3. Present in both</h3>
  <ul>
    <li><a href="./3-common_elements.py">3-common_elements.py</a>: Python function that returns a set of common elements in two sets.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>4. Only differents</h3>
  <ul>
    <li><a href="./4-only_diff_elements.py">4-only_diff_elements.py</a>: Python function that returns a set of all elements present in only one set.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>5. Number of keys</h3>
  <ul>
    <li><a href="./5-number_keys.py">5-number_keys.py</a>: Python function that returns the number of keys in a dictionary.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>6. Print sorted dictionary</h3>
  <ul>
    <li><a href="./6-print_sorted_dictionary.py">6-print_sorted_dictionary.py</a>: Python function that prints a dictionary by ordered keys.</li>
    <li>The function assumes all keys are strings.</li>
    <li>Keys are printed in alphabetic order.</li>
    <li>Keys are only sorted on the first level.</li>
    <li>Dictionary values can have any type.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>7. Update dictionary</h3>
  <ul>
    <li><a href="./7-update_dictionary.py">7-update_dictionary.py</a>: Python function that replaces or adds key/value pairs in a dictionary.</li>
    <li>The parameter <code>key</code> is always a string.</li>
    <li>The parameter <code>value</code> is any type.</li>
    <li>If a key exists in the dictionary, the value is replaced.</li>
    <li>If a key does not exist in the dictionary, it is created.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>8. Simple delete by key</h3>
  <ul>
    <li><a href="./8-simple_delete.py">8-simple_delete.py</a>: Python function that deletes a key in a dictionary.</li>
    <li>The parameter <code>key</code> is always a string.</li>
    <li>If the key does not exist, the dictionary does not change.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>9. Multiply by 2</h3>
  <ul>
    <li><a href="./9-multiply_by_2.py">9-multiply_by_2.py</a>: Python function that returns a new dictionary with all values multiplied by 2.</li>
    <li>Parameters:</li>
    <ul>
      <li><code>my_dict</code>: the dictionary to multiply the values.</li>
    </ul>
    <li>Returns a new dictionary with the same keys as <code>my_dict</code>, and the values multiplied by 2.</li>
    <li>The function assumes all values in the dictionary are integers.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>10. Best score</h3>
  <ul>
    <li><a href="./10-best_score.py">10-best_score.py</a>: Python function that returns a key-value pair with the highest integer value.</li>
    <li>Parameters:</li>
    <ul>
      <li><code>my_dict</code>: a dictionary with string keys and integer values.</li>
    </ul>
    <li>Returns the key-value pair with the highest integer value.</li>
    <li>The function assumes all values in the dictionary are integers.</li>
    <li>The function assumes all students have a different score.</li>
    <li>If no score is found, the function returns <code>None</code>.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>11. Multiply by using map</h3>
  <ul>
    <li><a href="./11-multiply_list_map.py">11-multiply_list_map.py</a>: Python function that returns a new list with all values multiplied by a number using <code>map</code>.</li>
    <li>Returns a new list of the same length as <code>my_list</code> with each value multiplied by <code>number</code>.</li>
    <li>The initial list is not modified.</li>
    <li>Without using loops or importing modules.</li>
  </ul>
  <h3>12. Roman to Integer</h3>
  <ul>
    <li><a href="./12-roman_to_int.py">12-roman_to_int.py</a>: Python function that converts a roman numeral to an integer.</li>
    <li>Parameters:</li>
    <ul>
      <li><code>roman_string</code>: a string representing a roman numeral.</li>
    </ul>
    <li>Returns the integer representation of the given roman numeral.</li>
    <li>The function assumes the number will be between 1-3999.</li>
    <li>If the parameter <code>roman_string</code> is not a string or <code>None</code>, the function returns <code>0</code>.</li>
  </ul>
  <h3>13. Weighted average!</h3>
  <ul>
    <li><a href="./100-weight_average.py">100-weight_average.py</a>: Python function that returns the weighted average of all integers in a list of tuples.</li>
    <li>Tuple format: <code>(<score>, <weight>)</code>.</li>
    <li>Returns the weighted average as a float.</li>
    <li>If the list is empty, returns <code>0</code>.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>14. Squared by using map</h3>
  <ul>
    <li><a href="./101-square_matrix_map.py">101-square_matrix_map.py</a>: Python function that computes the square value of all integers of a matrix using <code>map</code>.</li>
    <li>The parameter <code>matrix</code> is a two-dimensional array.</li>
    <li>Returns a new matrix of the same size as <code>matrix</code> with each value squared.</li>
    <li>The initial matrix is not modified.</li>
    <li>Without using loops or importing modules.</li>
  </ul>
  <h3>15. Delete by value</h3>
  <ul>
    <li><a href="./102-complex_delete.py">102-complex_delete.py</a>: Python function that deletes keys with a specific value in a dictionary.</li>
    <li>Parameters:</li>
    <ul>
      <li><code>my_dict</code>: a dictionary to delete keys from.</li>
      <li><code>value</code>: the value to search for and delete the corresponding keys.</li>
    </ul>
    <li>If the value does not exist, the dictionary remains unchanged.</li>
    <li>All keys having the searched value are deleted.</li>
    <li>Without importing modules.</li>
  </ul>
  <h3>16. CPython #1: PyBytesObject</h3>
  <ul>
    <li><a href="./103-python.c">103-python.c</a>: C functions that print basic information about Python lists and Python bytes objects.</li>
  </ul>
  <p>Feel free to explore and learn from the provided files. Enjoy coding!</p>
