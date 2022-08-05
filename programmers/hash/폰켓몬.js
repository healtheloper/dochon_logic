function solution(nums) {
  return new Set(nums).size > nums.length / 2
    ? nums.length / 2
    : new Set(nums).size;
}

// const solution = (nums) => Math.min(nums.length / 2, new Set(nums).size);
