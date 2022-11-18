const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;

  const [N, ...meetings] = input;
  let curEnd = 0;

  const meetingList = meetings.sort((a, b) => {
    const [aStart, aEnd] = a.split(' ').map((v) => +v);
    const [bStart, bEnd] = b.split(' ').map((v) => +v);
    if (aEnd === bEnd) {
      return aStart - bStart;
    }
    return aEnd - bEnd;
  });

  meetingList.forEach((meeting) => {
    const [start, end] = meeting.split(' ').map((v) => +v);
    if (start >= curEnd) {
      curEnd = end;
      answer += 1;
    }
  });
  return answer;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
