const isPrime = (num) => {
  for (let i = 2; i < num; i++) {
    if (num % i == 0) return false;
  }
  return true;
};
const getPermutations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
};
function solution(numbers) {
  var answer = 0;
  let result = [];
  for (let i = 1; i <= numbers.length; i++) {
    const nums = getPermutations([...numbers], i);
    for (const num of nums) {
      result.push(+num.join(""));
    }
  }
  result = result.filter((num) => isPrime(num));
  let set = [...new Set(result)];
  set = set.filter((element) => element !== 1 && element !== 0);
  answer = set.length;
  return answer;
}
