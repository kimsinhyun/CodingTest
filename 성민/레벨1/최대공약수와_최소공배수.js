function solution(n, m) {
  let a = Math.max(n, m);
  let b = Math.min(n, m);
  while (b != 0) {
    const r = a % b;
    a = b;
    b = r;
  }

  return [a, (n * m) / a];
}
