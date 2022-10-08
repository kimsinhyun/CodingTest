// function solution(N, stages) {
//   var answer = [];
//   let result = [];
//   let total = stages.length;
//   for (let i = 1; i <= N; i++) {
//     let count = 0;
//     let s_count = 0;
//     for (let item of stages) {
//       if (item < i) count++;
//       else if (item === i) s_count++;
//     }
//     result.push([i, s_count / (total - count)]);
//   }
//   result.sort((a, b) => b[1] - a[1]);
//   for (let item of result) {
//     answer.push(item[0]);
//   }
//   //console.log(answer);
//   return answer;
// }

function solution(N, stages) {
  let filterStages = stages;
  let currStagesLen = stages.length;
  const map = new Map();
  for (let i = 1; i <= N; i++) {
    filterStages = filterStages.filter((v) => v !== i);
    const value = (currStagesLen - filterStages.length) / currStagesLen;
    currStagesLen = filterStages.length;
    map.set(i, value);
  }
  return [...map.entries()].sort((a, b) => b[1] - a[1]).map((v) => v[0]);
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
