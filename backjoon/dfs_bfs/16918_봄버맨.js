const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [inputData, ...rest] = input;
  const [r, c, n] = inputData.split(" ");
  const bomb = [];
  let count = +n;
  const arr = rest.map((row) => row.split(""));
  let restBomb = new Array(+r).fill(null).map((v) => new Array(+c).fill("O"));
  arr.forEach((row, rowIdx) => {
    row.forEach((col, colIdx) => {
      if (col === "O") bomb.push([rowIdx, colIdx]);
    });
  });
  const bfs = () => {
    const q = [bomb];
    const dx = [0, 1, -1, 0, 0];
    const dy = [0, 0, 0, 1, -1];
    while (q.length > 0) {
      const v = q.shift();
      for (let i = 0; i < v.length; i++) {
        const [poX, poY] = v[i];
        for (let j = 0; j < 5; j++) {
          const a = poX + dx[j];
          const b = poY + dy[j];
          if (a < +r && a >= 0 && b < +c && b >= 0 && restBomb[a][b] == "O") {
            restBomb[a][b] = ".";
          }
        }
      }
      count -= 2;
      if (count > 2) {
        const newBomb = [];
        restBomb.forEach((row, rowIdx) => {
          row.forEach((col, colIdx) => {
            if (col === "O") newBomb.push([rowIdx, colIdx]);
          });
        });
        q.push(newBomb);
        restBomb = restBomb.map((v) => new Array(+c).fill("O"));
      }
    }
  };
  if (count === 1) {
    return arr.map((b) => b.join("")).reduce((a, b) => a + "\n" + b);
  } else if (count % 2 == 0) {
    return restBomb.map((b) => b.join("")).reduce((a, b) => a + "\n" + b);
  } else {
    bfs();
    return restBomb.map((b) => b.join("")).reduce((a, b) => a + "\n" + b);
  }
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
