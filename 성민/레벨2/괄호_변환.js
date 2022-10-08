//  균형잡힌 괄호 문자열: '('')' 갯수가 똑같은경우
//  올바른 괄호 문자열: 짝이 맞는 경우
/*
    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        4-3. ')'를 다시 붙입니다. 
        4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        4-5. 생성된 문자열을 반환합니다.
*/

function getBalanceBracket(s) {
  let newStr = "";
  let l = 0;
  let r = 0;
  let i = 0;
  for (const c of s) {
    if (l > 0 && r > 0 && l === r) break;
    if (c === ")") {
      newStr += ")";
      r++;
    } else if (c === "(") {
      newStr += "(";
      l++;
    }
    i++;
  }
  return [newStr, s.slice(i)];
}

function isBracket(s) {
  const stack = [];
  let l = 0;
  let r = 0;
  for (const c of s) {
    if (c === ")") {
      r++;
      if (stack[stack.length - 1] === "(") stack.pop();
    } else {
      l++;
      stack.push("(");
    }
  }
  if (stack.length === 0) return 1;
  else if (l === r) return 2;
  else return 0;
}

function transBracket(u, v) {
  let transU = "";
  for (const c of u.slice(1, u.length - 1)) {
    if (c === ")") transU += "(";
    else if (c === "(") transU += ")";
  }
  return "(" + v + ")" + transU;
}

function solution(p) {
  if (p.length === 0) return "";
  if (isBracket(p) === 1) return p;
  else {
    const [u, v] = getBalanceBracket(p);
    if (isBracket(u) === 1) return u + solution(v);
    else if (isBracket(u) === 2) {
      const restP = solution(v);
      return transBracket(u, restP);
    }
  }
}
