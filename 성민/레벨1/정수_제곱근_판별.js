function solution(n) {
  const root = Math.pow(n, 0.5);
  return Number.isInteger(root) ? (root + 1) * (root + 1) : -1;
}
