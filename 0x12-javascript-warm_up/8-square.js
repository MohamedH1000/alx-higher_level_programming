#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let a = 0; a < parseInt(process.argv[2]); a++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
