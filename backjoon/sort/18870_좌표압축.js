const input = require('fs')
  //   .readFileSync('/dev/stdin')
  .readFileSync(__dirname + '/18870.txt')
  .toString()
  .trim()
  .split('\n');

const solution = (input) => {
  const [N, rest] = input;
  const positions = rest.split(' ').map((v) => +v);
  const sortedPositions = [...new Set(positions)].sort((a, b) => a - b);
  const positionInfo = sortedPositions.reduce((acc, next, index) => {
    acc[next] = index;
    return acc;
  }, {});

  return positions
    .map((position) => {
      return positionInfo[position];
    })
    .join(' ');
};

console.log(solution(input));
