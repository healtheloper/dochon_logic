const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const [a, b, c] = input.split(" ").map((v) => BigInt(v));
  const pow = (a, b, c) => {
    if (b == 0) {
      return BigInt(1);
    }

    const temp = pow(a, BigInt(parseInt(b / BigInt(2))), c);
    if (b % BigInt(2) == 1) {
      return (((temp * temp) % c) * a) % c;
    } else {
      return (temp * temp) % c;
    }
  };

  return Number(pow(a, b, c));
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
