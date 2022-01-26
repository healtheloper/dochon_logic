function kangaroo(x1, v1, x2, v2) {
  // Write your code here
  if (v1 < v2) {
    return "NO";
  }
  return Number.isInteger((x2 - x1) / (v1 - v2)) ? "YES" : "NO";
}
