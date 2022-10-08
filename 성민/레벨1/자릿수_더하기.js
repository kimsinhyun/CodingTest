function solution(n) {
  let result = 0;
  String(n)
    .split("")
    .forEach((v) => (result += Number(v)));
  return result;
}
