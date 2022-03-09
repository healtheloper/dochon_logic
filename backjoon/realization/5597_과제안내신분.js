const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const numDict = {};
  Array(30)
    .fill(0)
    .forEach((v, i) => {
      numDict[i + 1] = true;
    });
  input.forEach((num) => {
    delete numDict[num];
  });
  return Object.keys(numDict).join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
