#!/usr/bin/node
const myVar = process.argv;
if (myVar.length <= 3) {
  console.log(0);
} else {
  console.log(myVar.sort(function (a, b) { return a - b; })[myVar.length - 2]);
}
