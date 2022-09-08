/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  return nums.findIndex((v, i) => {
    const left = nums.slice(0, i);
    const right = nums.slice(i + 1, nums.length);
    return (
      left.reduce((sum, next) => sum + next, 0) ===
      right.reduce((sum, next) => sum + next, 0)
    );
  });
};
