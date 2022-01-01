const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [num, people] = input;
  const peopleSort = people.split(" ").sort((a, b) => a - b);
  let sum = 0;
  for (let i = 0; i < peopleSort.length; i++) {
    for (let j = 0; j < i + 1; j++) {
      sum += +peopleSort[j];
    }
  }
  return sum;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
