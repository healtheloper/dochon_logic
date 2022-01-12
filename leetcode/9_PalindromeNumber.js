/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
  return x + "" === [...(x + "")].reverse().join("");
};
