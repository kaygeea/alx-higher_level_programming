#!/usr/bin/node
/*
 * Print message based on argument vector count.
 * SPECS:
 * -> If no arguments are passed to the script, print “No argument”.
 * -> If only one argument is passed to the script, print “Argument found”.
 * -> Otherwise, print “Arguments found”.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 */

if (process.argv[2] === undefined) {
  console.log('No arguemnt');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
