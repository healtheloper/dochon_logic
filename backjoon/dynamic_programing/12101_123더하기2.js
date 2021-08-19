const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (n, k) => {
  let answer = [0];
  const first = ["1"];
  const second = ["1+1", "2"];
  const third = ["1+1+1", "1+2", "2+1", "3"];
  answer.push(first);
  answer.push(second);
  answer.push(third);
  for (let i = 4; i <= n; i++) {
    let temp = [];
    temp.push(answer[i - 1].map((el) => "1+" + el));
    temp.push(answer[i - 2].map((el) => "2+" + el));
    temp.push(answer[i - 3].map((el) => "3+" + el));
    answer.push(temp.flat());
  }
  return answer[n][k - 1] ? answer[n][k - 1] : -1;
};

rl.on("line", (answer) => {
  const [n, k] = answer.split(" ");
  console.log(solution(n, k));
  rl.close();
});
