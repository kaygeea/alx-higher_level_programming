#!/usr/bin/node
/* Print 'C is fun' x times.
 * SPECS:
 * -> Where x is the first argument of the script.
 * -> If the first argument can’t be converted to an integer, print “Missing number of occurrences”.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 * -> "console.log()" can only be used two times in the code.
 * -> Use of a loop (while, for, etc) is mandatory.
 */

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
