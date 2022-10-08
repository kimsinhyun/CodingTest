function solution(n) {
  var answer = 0;
  answer = +n
    .toString()
    .split("")
    .sort((a, b) => b - a)
    .map((e) => +e)
    .join("");
  return answer;
}
