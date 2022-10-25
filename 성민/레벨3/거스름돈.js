function solution(n, money) {
  var answer = 0;
  let dp = Array(n + 1).fill(0);
  dp[0] = 1;
  money.forEach((el, idx) => {


