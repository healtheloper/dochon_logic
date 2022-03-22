const isPrime = (num) => {
  if (num === 1) return true;
  return Array(num - 2)
    .fill(0)
    .map((_, i) => i + 2)
    .every((v) => num % v !== 0);
};

const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((v) => [v]);
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((v) => [fixed, ...v]);
    results.push(...attached);
  });
  return results;
};

function solution(nums) {
  const comb = getCombinations(nums, 3);
  return comb.filter((arr) => isPrime(arr.reduce((acc, val) => acc + val)))
    .length;
}
