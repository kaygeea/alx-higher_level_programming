#!/usr/bin/node
/* Print a square with the 'x' character.
 * SPECS:
 * -> The first argument is the size of the square.
 * -> If the first argument can’t be converted to an integer, print “Missing size”.
 * -> The square should be printed out with the 'x' character.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 * -> Use of a loop (while, for, etc) is mandatory.
 */

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let yAxis = 0; yAxis < num; yAxis++) {
    let row = '';
    for (let xAxis = 0; xAxis < num; xAxis++) {
      row += 'x';
    }
    console.log(row);
  }
}
