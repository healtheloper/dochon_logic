function solution(strings, n) {
  return strings.sort((c1, c2) => {
    if (c1[n] === c2[n]) return c1 > c2 ? 1 : -1;
    return c1[n] > c2[n] ? 1 : -1;
  });
}
