const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [counts, ...rest] = input;
  const [N, M, B] = counts.split(' ').map((v) => +v);
  const floors = rest.map((array) => array.split(' ').map((v) => +v));
  const allFloors = floors.flat();
  const maxFloor = Math.max(...allFloors);
  let minTime = 1e9;
  let minFloor = maxFloor;
  for (let i = maxFloor; i >= 0; i--) {
    let block = B;
    let time = 0;
    for (let j = 0; j < N * M; j++) {
      const floor = allFloors[j];
      const floorDiff = Math.abs(i - floor);
      if (i < floor) {
        block += floorDiff;
        time += floorDiff * 2;
      } else if (i > floor) {
        block -= floorDiff;
        time += floorDiff;
      }
    }
    if (block >= 0 && time < minTime) {
      minTime = time;
      minFloor = i;
    }
  }
  return `${minTime} ${minFloor}`;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
