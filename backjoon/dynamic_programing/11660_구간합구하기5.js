const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const getReformArray = (array) => {
  const temp = [...array];
  for (let i = 0; i < temp.length - 2; i++) {
    temp[0][i + 1] += temp[0][i];
    temp[i + 1][0] += temp[i][0];
  }
  for (let i = 0; i < temp.length - 1; i++) {
    for (let j = 0; j < temp.length - 1; j++) {
      temp[i + 1][j + 1] += temp[i][j + 1] + temp[i + 1][j] - temp[i][j];
    }
  }
  temp.map((v) => v.pop());
  temp.pop();
  return temp;
};
const solution = (input) => {
  let answer = [];
  const array = [];
  const [inputs, ...rest] = input;
  const [n, m] = inputs.split(" ").map((v) => +v);
  for (let i = 0; i < n; i++) {
    const row = rest[i].split(" ").map((v) => +v);
    row.push(0);
    array.push(row);
  }
  array.push(new Array(n + 1).fill(0));
  const reformArray = getReformArray(array);
  for (let j = 0; j < m; j++) {
    const [x1, y1, x2, y2] = rest[n + j].split(" ").map((v) => +v);
    let sum = reformArray[x2 - 1][y2 - 1];
    if (x1 - 2 >= 0 && y2 - 1 >= 0) {
      sum -= reformArray[x1 - 2][y2 - 1];
    }
    if (x2 - 1 >= 0 && y1 - 2 >= 0) {
      sum -= reformArray[x2 - 1][y1 - 2];
    }
    if (x1 - 2 >= 0 && y1 - 2 >= 0) {
      sum += reformArray[x1 - 2][y1 - 2];
    }
    answer.push(sum);
  }
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
