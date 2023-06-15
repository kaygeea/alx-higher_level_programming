#!/usr/bin/node
/* Update given script to replace 12 as "value" with 98.
 *
 * CONSTRAINTS:
 * -> Use of "var" is not allowed.
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89; // Properties of objects assigned to constants are not protected; thus they can be changed.
console.log(myObject);
