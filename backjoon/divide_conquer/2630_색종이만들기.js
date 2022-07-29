const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const solution = (input) => {
  const [N, ...rest] = input;
  let blue = 0;
  let white = 0;
  const 색종이 = rest.map((row) => row.split(' ').map((v) => +v));

  const 판단 = (startPosition, size) => {
    const [x, y] = startPosition;
    let thisColor = -1;
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        if (i === 0 && j === 0) {
          thisColor = 색종이[x + i][y + j];
          continue;
        }
        if (색종이[x + i][y + j] !== thisColor) {
          const newSize = Math.floor(size / 2);
          const startPositions = [
            [x, y],
            [x + newSize, y],
            [x, y + newSize],
            [x + newSize, y + newSize],
          ];
          startPositions.forEach((position) => {
            판단(position, newSize);
          });
          return;
        }
      }
    }
    if (thisColor === 1) blue += 1;
    else white += 1;
  };

  판단([0, 0], +N);

  return [white, blue].join('\n');
};

console.log(solution(input));
