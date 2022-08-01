#!/usr/bin/node
const myVar = process.argv;
if (myVar[2] && myVar[3]) {
  console.log(myVar[2] + ' is ' + myVar[3]);
} else if (myVar[2]) {
  console.log(myVar[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
