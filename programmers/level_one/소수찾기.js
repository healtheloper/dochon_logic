function solution(n) {
  let count = 0;
  // 1_000_000
  for (let i = 2; i <= n; i++) {
    let flag = true;
    // 1_000
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        flag = false;
        break;
      }
    }
    if (flag) {
      count += 1;
    }
  }
  return count;
}
