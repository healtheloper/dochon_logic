/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const sortedNums = [...nums]
    .map((val, idx) => [val, idx])
    .sort((a, b) => a[0] - b[0]);

  for (let i = 0; i < sortedNums.length; i++) {
    const v1 = sortedNums[i][0];
    const v2 = target - v1;
    let low = i + 1;
    let high = sortedNums.length - 1;
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);
      if (v2 < sortedNums[mid][0]) {
        high = mid - 1;
      } else if (v2 > sortedNums[mid][0]) {
        low = mid + 1;
      } else {
        return [sortedNums[i][1], sortedNums[mid][1]];
      }
    }
  }
};
