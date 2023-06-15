#!/usr/bin/node
/* Define function that adds two integers and prints the sum.
 * SPECS:
 * -> The first argument is the first integer.
 * -> The second argument is the second integer.
 * -> Define a function with this prototype: "function add(a, b)"
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 */

function add (a, b) {
  return a + b;
}

console.log(add(parseInt(a, 10), parseInt(b, 10)));
