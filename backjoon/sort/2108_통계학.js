const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [count, ...arr] = input;

  const sum = arr.reduce((a, b) => +a + +b);
  const sort = arr.sort((a, b) => +a - +b);
  const counts = {};
  arr.forEach((v, i) => {
    if (counts[v]) counts[v]++;
    else counts[v] = 1;
  });

  const counts_sort = Object.entries(counts).sort(([c, a], [d, b]) => {
    if (a == b) {
      return c - d;
    }
    return b - a;
  });

  let most_value;
  if (counts_sort.length > 1 && counts_sort[0][1] == counts_sort[1][1]) {
    most_value = counts_sort[1][0];
  } else {
    most_value = counts_sort[0][0];
  }
  const range = sort[sort.length - 1] - sort[0];
  return [
    Math.round(sum / count),
    sort[parseInt(sort.length / 2)],
    most_value,
    range,
  ].join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
