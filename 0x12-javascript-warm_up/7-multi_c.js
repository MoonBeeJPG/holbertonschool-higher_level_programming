#!/usr/bin/node
const myVar = process.argv;
if (myVar[2]) {
  for (let i = 0; i < parseInt(myVar[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
