const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const answer = [];

  const [count, ...rest] = input;
  let idx = 0;
  const result = [];
  const temp = [];
  for (let i = 1; i <= count; i++) {
    if (rest[idx] == i) {
      result.push(i);
      answer.push("+");
      answer.push("-");
      idx++;
      for (let j = temp.length - 1; j >= 0; j--) {
        if (temp[j] == rest[idx]) {
          answer.push("-");
          result.push(temp.pop());
          idx++;
        } else {
          break;
        }
      }
    } else {
      answer.push("+");
      temp.push(i);
    }
  }
  return temp.length > 0 ? "NO" : answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
