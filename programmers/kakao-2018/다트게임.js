function solution(dartResult) {
  let answer = [];
  let number = '';

  for (let i = 0; i < dartResult.length; i++) {
    const result = dartResult[i];
    if (!isNaN(Number(result))) {
      number += result;
      continue;
    }
    if (number !== '') {
      answer.push(+number);
    }
    if (result === '*') {
      if (answer.length === 1) {
        answer[0] *= 2;
      } else {
        answer[answer.length - 1] *= 2;
        answer[answer.length - 2] *= 2;
      }
    } else if (result === '#') {
      answer[answer.length - 1] *= -1;
    } else if (result === 'S') {
      answer[answer.length - 1] **= 1;
    } else if (result === 'D') {
      answer[answer.length - 1] **= 2;
    } else if (result === 'T') {
      answer[answer.length - 1] **= 3;
    }
    number = '';
  }
  return answer.reduce((sum, next) => sum + next, 0);
}
