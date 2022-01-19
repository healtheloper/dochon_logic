const checkPop = (array, element) => {
  if (array[array.length - 1] === element) {
    return true;
  }
  return false;
};

function solution(board, moves) {
  const stack = [];
  let answer = 0;
  moves.forEach((move) => {
    for (let i = 0; i < board.length; i++) {
      const element = board[i][move - 1];
      if (element !== 0) {
        const check = checkPop(stack, element);
        if (check) {
          stack.pop();
          answer += 2;
        } else {
          stack.push(element);
        }
        board[i][move - 1] = 0;
        break;
      }
    }
  });
  return answer;
}
