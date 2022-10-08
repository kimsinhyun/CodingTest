function isBracket(index, s) {
  const stack = [];
  let i = index;
  let cnt = 0;
  while (cnt < s.length) {
    if (s[i] === "]") {
      if (stack[stack.length - 1] !== "[") return false;
      else stack.pop();
    } else if (s[i] === ")") {
      if (stack[stack.length - 1] !== "(") return false;
      else stack.pop();
    } else if (s[i] === "}") {
      if (stack[stack.length - 1] !== "{") return false;
      else stack.pop();
    } else {
      stack.push(s[i]);
    }
    cnt++;
    i = i + 1 === s.length ? 0 : i + 1;
  }
  return stack.length === 0 ? true : false;
}
function solution(s) {
  let answer = 0;
  const strLen = s.length;
  let i = 0;

  while (i < strLen) {
    if (isBracket(i, s)) answer++;
    i++;
  }
  return answer;
}

console.log(solution("[](){}"));
