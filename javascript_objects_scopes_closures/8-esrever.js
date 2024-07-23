#!/usr/bin/node
function reverse (list) {
  const out = [];
  for (let i = list.length - 1; i >= 0; i--) {
    out.push(list[i]);
  }
  return out;
}
exports.esrever = reverse;
