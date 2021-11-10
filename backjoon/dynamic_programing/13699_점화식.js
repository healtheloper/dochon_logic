const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const arr = [BigInt(1)];
  for (let i = 1; i <= 35; i++) {
    let temp = BigInt(0);
    for (let j = 0; j < i; j++) {
      temp += arr[j] * arr[i - j - 1];
    }
    arr.push(temp);
  }

  return arr[input];
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
