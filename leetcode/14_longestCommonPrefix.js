/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = (strs) => {
  let baseStr = strs[0];
  return strs.reduce((commonPrefix, nextStr) => {
    let newPrefix = "";
    for (let i = 0; i < commonPrefix.length; i++) {
      if (nextStr[i] === commonPrefix[i]) {
        newPrefix += commonPrefix[i];
      } else {
        return newPrefix;
      }
    }
    return newPrefix;
  }, baseStr);
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
