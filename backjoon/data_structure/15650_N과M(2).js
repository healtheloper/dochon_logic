const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const getCombinations = (arr, num) => {
  const results = [];
  if (num == 1) return arr.map((v) => [v]);
  arr.forEach((value, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, num - 1);
    const attached = combinations.map((v) => [value, ...v]);
    results.push(...attached);
  });
  return results;
};
const solution = (input) => {
  const [n, m] = input[0].split(" ").map((v) => +v);
  const array = new Array(n).fill(null).map((v, i) => i + 1);
  const answer = getCombinations(array, m).map((arr) => arr.join(" "));
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
