function solution(citations) {
  var answer = 0;
  citations.sort((a, b) => a - b);
  const max_val = citations[citations.length - 1];
  for (let i = 0; i < max_val; i++) {
    let count = 0;
    for (const item of citations) {
      if (item >= i) {
        count++;
      }
      if (count >= i) {
        if (answer < count) answer = i;
      }
    }
  }
  return answer;
}
