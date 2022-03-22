function solution(lottos, win_nums) {
  const hasWin = lottos.filter((v) => win_nums.includes(v)).length;
  const zeros = lottos.filter((v) => v === 0).length;
  const win = [6, 6, 5, 4, 3, 2, 1];
  return [win[hasWin + zeros], win[hasWin]];
}
