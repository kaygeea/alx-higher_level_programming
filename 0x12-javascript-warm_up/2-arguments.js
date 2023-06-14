#!/usr/bin/node
// Print message based on argument vector count.

if (process.argv.length === 2) {
  console.log('No arguemnt');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
