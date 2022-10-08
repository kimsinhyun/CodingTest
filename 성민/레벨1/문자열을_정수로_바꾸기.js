function solution(s) {
  var answer = 0;
  if (s[0] === "-") {
    return -Number(s.slice(1));
  }
  return Number(s);
}
