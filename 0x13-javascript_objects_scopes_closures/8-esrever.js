#!/usr/bin/node

exports.esrever = function (list) {
  let listNew = [];
  for (let cent = list.length - 1; cent >= 0; cent--) {
    listNew.push(list[cent]);
  }
  return listNew;
};
