#!/usr/bin/node
/* Print "My number: <first argument converted in integer>", if the first arg passed
 * can be converted to an integer.
 * SPECS:
 * -> If the argument can’t be converted to an integer, print “Not a number”.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 * -> Use of "try/catch" is not allowed.
 */

if (process.argv) {
  const num = parseInt(process.argv[2], 10);
  if (Number.isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
}
