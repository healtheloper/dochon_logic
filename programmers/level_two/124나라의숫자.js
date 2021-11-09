function solution(n) {
  const pattern = [1, 2, 4];
  let str = "";
  const toPattern = (n) => {
    const m = parseInt((n - 1) / 3);
    const r = (n - 1) % 3;
    str = pattern[r] + str;
    if (m >= 3) return toPattern(m);
    else return m !== 0 ? pattern[m - 1] + str : str;
  };
  return toPattern(n);
}
