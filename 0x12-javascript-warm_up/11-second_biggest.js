#!/usr/bin/node
/* Search for the second biggest integer in the list of arguments.
 * SPECS:
 * -> It can be assumed that all arguments can be converted to integer.
 * -> Print 0, if no arguments are passed.
 * -> Print 0, if only 1 argument is passed.
 *
 * CONSTRAINTS:
 * -> "console.log()" must be used to print all outputs.
 * -> Use of "var" is not allowed.
 */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
