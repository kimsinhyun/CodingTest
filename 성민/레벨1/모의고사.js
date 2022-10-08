function getAnswerCnt(answers, userAnswers) {
  let answer = 0;
  let temp = 0;
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === userAnswers[temp]) {
      answer++;
    }
    if (temp === userAnswers.length - 1) {
      temp = 0;
    } else {
      temp++;
    }
  }
  return answer;
}
function solution(answers) {
  const answer = [];
  const user1 = [1, 2, 3, 4, 5];
  const user2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const u1AnsCnt = getAnswerCnt(answers, user1);
  const u2AnsCnt = getAnswerCnt(answers, user2);
  const u3AnsCnt = getAnswerCnt(answers, user3);
  const maxCnt = Math.max(u1AnsCnt, u2AnsCnt, u3AnsCnt);
  console.log(u1AnsCnt, u2AnsCnt, u3AnsCnt);
  if (u1AnsCnt === maxCnt) answer.push(1);
  if (u2AnsCnt === maxCnt) answer.push(2);
  if (u3AnsCnt === maxCnt) answer.push(3);
  return answer;
}

solution([1, 2, 3, 4, 5]);
// function solution(answers) {
//   var answer = [];
//   let a = [1, 2, 3, 4, 5];
//   let b = [2, 1, 2, 3, 2, 4, 2, 5];
//   let c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
//   let len = [];
//   let j = 0;
//   let max = 0;
//   let as = 0;
//   let bs = 0;
//   let cs = 0;
//   for (let i = 0; i < answers.length; i++) {
//     if (answers[i] === a[i > 4 ? i % 5 : i]) as++;
//     if (answers[i] === b[i > 7 ? i % 8 : i]) bs++;
//     if (answers[i] === c[i > 9 ? i % 10 : i]) cs++;
//   }
//   len = [as, bs, cs];
//   max = Math.max(as, bs, cs);
//   for (let k = 0; k < 3; k++) {
//     if (max === len[k]) {
//       answer[j] = k + 1;
//       j++;
//     }
//   }
//   return answer;
// }
