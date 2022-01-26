function diagonalDifference(arr) {
  // Write your code here
  let first = 0;
  let last = arr[0].length - 1;
  let d1 = 0;
  let d2 = 0;
  for (let i = 0; i < arr.length; i++) {
    d1 += arr[i][first];
    d2 += arr[i][last];
    first += 1;
    last -= 1;
  }
  return Math.abs(d1 - d2);
}
