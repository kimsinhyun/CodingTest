function solution(progresses, speeds) {
  const answer = [];

  while (progresses.length) {
    let completeCnt = 0;
    for (let i = 0; i < progresses.length; i++) {
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      }
    }
    while (progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      completeCnt++;
    }
    if (completeCnt) {
      answer.push(completeCnt);
    }
  }
  return answer;
}

console.log(solution([99, 99, 99, 90, 90, 90], [1, 1, 1, 1, 1, 1]));
