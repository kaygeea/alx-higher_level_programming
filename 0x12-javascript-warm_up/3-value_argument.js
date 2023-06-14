#!/usr/bin/node
/* Print the first argument passed to script.
 * SPECS:
 * -> If no arguments are passed to the script, print “No argument”.
 * -> "console.log()" must be used to print all outputs.
 *
 * CONSTRAINTS:
 * -> Not allowed to use "var".
 * -> Not allowed to use "length".
 */

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
