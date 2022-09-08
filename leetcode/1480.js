/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  return nums.map((v, i) =>
    nums.reduce((sum, next, index) => {
      if (index <= i) return sum + next;
      return sum;
    }, 0)
  );
};
