const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const wordDict = {
    pi: true,
    ka: true,
    chu: true,
  };
  const words = [...input];
  const correct = words.reduce((prev, next) => {
    let str = prev + next;
    if (wordDict[str]) return "";
    else return str;
  }, "");
  if (correct.length === 0) return "YES";
  else return "NO";
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
