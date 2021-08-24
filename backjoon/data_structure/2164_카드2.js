const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const arr = new Array(+input).fill(null).map((v, i) => i + 1);
  let list = arr;
  let even = true;
  while (list.length > 1) {
    if (even) {
      if (list.length % 2 !== 0) even = !even;
      list = list.filter((a, i) => i % 2 !== 0);
    } else {
      if (list.length % 2 !== 0) even = !even;
      list = list.filter((a, i) => i % 2 === 0);
    }
  }
  return list[0];
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
