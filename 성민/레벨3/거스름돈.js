function solution(n, money) {
  var answer = 0;
  let dp = Array(n + 1).fill(0);
  dp[0] = 1;
  money.forEach((el, idx) => {
    for (let i = el; i < n + 1; i++) {
      dp[i] += dp[i - el];
    }
  });
  answer = dp[n] % 1000000007;
  return answer;
}
