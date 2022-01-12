const reverse = (x) => {
  const isMinus = x < 0 ? true : false;
  const reverseX = [...(Math.abs(x) + "")].reverse().join("");
  const answer = isMinus ? -reverseX : +reverseX;
  return answer <= 2 ** 31 - 1 && answer >= -(2 ** 31) ? answer : 0;
};

console.log(reverse(1534236469));
