function solution(answers) {
  const user1 = { idx: 1, count: 0, pattern: [1, 2, 3, 4, 5] };
  const user2 = { idx: 2, count: 0, pattern: [2, 1, 2, 3, 2, 4, 2, 5] };
  const user3 = { idx: 3, count: 0, pattern: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] };
  answers.forEach((answer, answerIdx) => {
    [user1, user2, user3].forEach((user) => {
      if (user.pattern[answerIdx % user.pattern.length] === answer) {
        user.count += 1;
      }
    });
  });
  const maxCount = Math.max(user1.count, user2.count, user3.count);
  return [user1, user2, user3]
    .filter((user) => user.count === maxCount)
    .map((v) => v.idx);
}
