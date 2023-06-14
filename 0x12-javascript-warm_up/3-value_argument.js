#!/usr/bin/node
/* Print the first argument passed to script.
 * SPECS:
 * -> If no arguments are passed to the script, print “No argument”.
 * -> "console.log()" must be used to print all outputs.
 *
 * RESTRICTIONS:
 * -> Not allowed to use "var".
 * -> Not allowed to use "length".
 */

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
