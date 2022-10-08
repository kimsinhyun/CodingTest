function solution(arr1, arr2) {
  var answer = [];
  const colLen = arr1.length;
  const rowLen = arr1[0].length;
  for (let i = 0; i < colLen; i++) {
    answer.push([]);
    for (let j = 0; j < rowLen; j++) {
      answer[i].push(arr1[i][j] + arr2[i][j]);
    }
  }
  return answer;
}
