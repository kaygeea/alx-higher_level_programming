#!/usr/bin/node
/* Make a function "visible from outside".
 * SPECS:
 * -> The name of the function must be add.
 *
 * CONSTRAINTS:
 * -> Use of "var" is not allowed.
 */

exports.add = (a, b) => a + b;
