function solution(n, arr1, arr2) {
  const answer = [];
  for (let i = 0; i < n; i++) {
    const sum = Number(arr1[i].toString(2)) + Number(arr2[i].toString(2));
    const r =
      String(sum).length < n
        ? '0'.repeat(n - String(sum).length) + String(sum)
        : String(sum);
    answer.push([...r].map((v) => (v === '0' ? ' ' : '#')).join(''));
  }
  return answer;
}
