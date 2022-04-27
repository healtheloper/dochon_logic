function solution(numbers) {
  return Array(9)
    .fill(0)
    .map((v, i) => i + 1)
    .reduce((sum, next) => {
      if (!numbers.includes(next)) sum += next;
      return sum;
    }, 0);
}
