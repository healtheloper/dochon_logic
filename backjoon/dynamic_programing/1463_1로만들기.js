const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const array = new Array(+input + 1).fill(0);
  array[2] = 1;
  array[3] = 1;

  for (let i = 4; i < array.length; i++) {
    if (i % 3 == 0 && i % 2 == 0) {
      array[i] = Math.min(array[i / 2], array[i / 3], array[i - 1]) + 1;
    } else if (i % 3 == 0) {
      array[i] = Math.min(array[i / 3], array[i - 1]) + 1;
    } else if (i % 2 == 0) {
      array[i] = Math.min(array[i / 2], array[i - 1]) + 1;
    } else {
      array[i] = array[i - 1] + 1;
    }
  }
  return array[+input];
};

rl.on('line', (answer) => {
  console.log(solution(answer));
  rl.close();
});
