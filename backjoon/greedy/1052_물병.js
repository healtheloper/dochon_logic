const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let answer = 0;
  const bottles = [];
  const [n, k] = input.split(" ").map((v) => +v);
  let weight = 0;
  let bottleCount = n;
  while (bottleCount >= 1) {
    const isOdd = bottleCount % 2 == 1;
    if (isOdd) {
      bottleCount -= 1;
      bottles.push(weight);
    }
    bottleCount /= 2;
    weight += 1;
  }
  if (bottles.length <= k) return 0;

  const remainBottles = bottles.slice(0, bottles.length - k + 1);

  const start = remainBottles[0];
  const end = remainBottles[remainBottles.length - 1];
  let sum = 2 ** start;
  for (let i = start + 1; i < end; i++) {
    if (!remainBottles.includes(i)) sum += 2 ** i;
  }
  return sum;
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
