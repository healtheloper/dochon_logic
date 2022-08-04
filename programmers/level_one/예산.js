function solution(d, budget) {
  const sortedD = d.sort((a, b) => a - b);
  let newBudget = budget;
  let result = 0;

  for (let i = 0; i < sortedD.length; i++) {
    const cost = sortedD[i];
    newBudget -= cost;
    if (newBudget < 0) {
      break;
    }
    result += 1;
  }

  return result;
}
