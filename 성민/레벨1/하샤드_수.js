function solution(x) {
  const total = String(x)
    .split("")
    .reduce((pre, curr) => Number(pre) + Number(curr), 0);
  return x % total === 0 ? true : false;
}
