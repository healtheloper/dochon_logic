function solution(price, money, count) {
  const result =
    Array(count)
      .fill(0)
      .reduce((acc, next, idx) => acc + price * (idx + 1), 0) - money;
  return result > 0 ? result : 0;
}
