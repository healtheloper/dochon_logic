const getDistance = (p1, p2) => {
  const [x1, y1] = p1;
  const [x2, y2] = p2;
  return Math.abs(x2 - x1) + Math.abs(y2 - y1);
};

function solution(numbers, hand) {
  let answer = '';

  const positions = [
    [3, 1],
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
  ];
  let leftPosition = [3, 0];
  let rightPosition = [3, 2];
  numbers.forEach((number) => {
    const position = positions[number];
    if (number == 1 || number == 4 || number == 7) {
      leftPosition = position;
      answer += 'L';
    } else if (number == 3 || number == 6 || number == 9) {
      rightPosition = position;
      answer += 'R';
    } else {
      const leftDistance = getDistance(leftPosition, position);
      const rightDistance = getDistance(rightPosition, position);
      if (leftDistance > rightDistance) {
        rightPosition = position;
        answer += 'R';
      } else if (leftDistance < rightDistance) {
        leftPosition = position;
        answer += 'L';
      } else {
        if (hand === 'right') {
          rightPosition = position;
          answer += 'R';
        } else {
          leftPosition = position;
          answer += 'L';
        }
      }
    }
  });
  return answer;
}
