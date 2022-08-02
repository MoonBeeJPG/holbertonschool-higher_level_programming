#!/usr/bin/node
const myVar = process.argv;
function factoralize (num) {
  return (num * factoralize(num - 1));
}
if (myVar[2]) {
  console.log(factoralize(parseInt(myVar[2])));
} else {
  console.log(1);
}
