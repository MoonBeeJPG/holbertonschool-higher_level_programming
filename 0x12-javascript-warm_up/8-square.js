#!/usr/bin/node
const myVar = process.argv;
if (parseInt(myVar[2])) {
  for (let i = 0; i < parseInt(myVar[2]); i++) {
    console.log('X'.repeat(myVar[2]));
  }
} else {
  console.log('Missing size');
}
