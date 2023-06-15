#!/usr/bin/node
/* Define a function that computes and print the factorial of a number
 * SPECS:
 * -> The first argument is an integer (can be casted as int) used for computing the factorial.
 * -> Factorial of NaN is 1
 *
 * CONSTRAINTS:
 * -> A function must be used.
 * -> The function must execute recursively.
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 */

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return 'Positive numbers only!';
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const input = parseInt(process.argv[2], 10);
console.log(factorial(input));
