const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  const [count, ...rest] = input;
  const string = rest[0].split("");
  let nums = string.map((char) => char.charCodeAt() - 96);
  let mulR = 1;
  for (let i = 0; i < count; i++) {
    answer += (nums[i] * mulR) % 1234567891;
    mulR *= 31;
    mulR %= 1234567891;
    answer %= 1234567891;
  }
  return answer;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
