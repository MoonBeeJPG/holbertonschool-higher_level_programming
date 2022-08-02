#!/usr/bin/node
const myVar = process.argv;
function add (a, b) {
  return a + b;
}
if (myVar[2] && myVar[3]) {
  console.log(add(parseInt(myVar[2]), parseInt(myVar[3])));
} else {
  console.log('NaN');
}
