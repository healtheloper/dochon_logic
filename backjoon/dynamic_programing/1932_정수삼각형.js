const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [_, ...tri] = input;
  const triArr = tri.map((v) => v.split(" ").map((v) => +v));

  for (let i = 1; i < triArr.length; i++) {
    const row = triArr[i];
    for (let j = 0; j < row.length; j++) {
      if (j == 0) {
        row[j] += triArr[i - 1][j];
      } else if (j == row.length - 1) {
        row[j] += triArr[i - 1][j - 1];
      } else {
        row[j] += Math.max(triArr[i - 1][j], triArr[i - 1][j - 1]);
      }
    }
  }
  return Math.max(...triArr[triArr.length - 1]);
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
