const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = ([info, ...rest]) => {
  let answer = 0;
  const [m, n, h] = info.split(" ");
  let temp = [];
  const floorArray = [];
  const tomato = [];

  for (let i = 0; i < rest.length; i++) {
    if (temp.length < +n) {
      temp.push(rest[i].split(" ").map((v) => +v));
    }
    if (temp.length === +n) {
      floorArray.push(temp);
      temp = [];
    }
  }

  const bfs = (tomato, floorArray) => {
    const q = [tomato];
    let count = 0;
    const dx = [1, -1, 0, 0, 0, 0];
    const dy = [0, 0, 1, -1, 0, 0];
    const dh = [0, 0, 0, 0, 1, -1];

    while (q.length > 0) {
      const v = q.shift();
      const temp_q = [];
      for (let i = 0; i < v.length; i++) {
        const [a, b, c] = v[i];
        for (let j = 0; j < 6; j++) {
          z = a + dh[j];
          x = b + dy[j];
          y = c + dx[j];
          if (
            x >= 0 &&
            x < n &&
            y >= 0 &&
            y < m &&
            z >= 0 &&
            z < h &&
            floorArray[z][x][y] === 0
          ) {
            temp_q.push([z, x, y]);
            floorArray[z][x][y] = 1;
          }
        }
      }
      if (temp_q.length > 0) {
        count += 1;
        q.push(temp_q);
      }
    }
    return count;
  };

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < m; k++) {
        if (floorArray[i][j][k] === 1) {
          tomato.push([i, j, k]);
        }
      }
    }
  }
  answer = bfs(tomato, floorArray);

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < m; k++) {
        if (floorArray[i][j][k] === 0) {
          answer = -1;
        }
      }
    }
  }
  return answer;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
