function solution(arr) {
  const total = arr.reduce((pre, curr) => pre + curr, 0);
  return total / arr.length;
}
