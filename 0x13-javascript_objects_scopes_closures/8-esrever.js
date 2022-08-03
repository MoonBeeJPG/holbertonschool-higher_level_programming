#!/usr/bin/node
exports.esrever = function (list) {
  const listt = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listt.push(list[i]);
  }
  return (listt);
};
