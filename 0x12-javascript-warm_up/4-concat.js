#!/usr/bin/node
/* Concatenate then Print 2 arguemnts passed; while adding "is" in between.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 */

if (process.argv) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
