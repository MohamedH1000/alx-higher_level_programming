#!/usr/bin/node

if (process.argv.length <= 3 || isNaN(process.argv)) {
  console.log(0);
} else {
  const array = process.argv.sort();
  console.log(array.reverse()[1]);
}
