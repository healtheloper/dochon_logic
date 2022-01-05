const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let answer = [];
  let [a, b] = input.split(" ").map((v) => [...v].map((v) => +v).reverse());
  const maxLength = Math.max(a.length, b.length);
  if (a.length !== maxLength) {
    a = [...a, ...new Array(maxLength - a.length).fill(0)];
  } else {
    b = [...b, ...new Array(maxLength - b.length).fill(0)];
  }
  let carryIn = 0;
  for (let i = 0; i < maxLength; i++) {
    const sum = (a[i] + b[i] + carryIn) % 10;
    const carryOut = parseInt((a[i] + b[i] + carryIn) / 10);

    answer.push(sum);
    carryIn = carryOut;
  }
  if (carryIn !== 0) answer.push(carryIn);
  return answer.reverse().join("");
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
