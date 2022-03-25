function solution(num) {
  let count = 0;
  let n = num;
  while (n !== 1) {
    if (count === 500) return -1;
    n = n % 2 === 0 ? n / 2 : n * 3 + 1;
    count += 1;
  }
  return count;
}
