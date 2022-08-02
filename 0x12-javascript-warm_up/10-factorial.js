#!/usr/bin/node
const myVar = process.argv;
function factoralize (num) {
  if (num === 0) {
    return 1;
  } else {
    return (num * factoralize(num - 1));
  }
}
if (myVar[2]) {
  console.log(factoralize(parseInt(myVar[2])));
} else if (!myVar[2]) {
  console.log(1);
}
