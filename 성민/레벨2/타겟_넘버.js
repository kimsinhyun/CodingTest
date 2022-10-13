function solution(numbers, target) {
  let answer = 0;
  const arr = [[+numbers[0], -numbers[0]]];
  for (let i = 1; i < numbers.length; i++) {
    const tempArr = [];
    for (const number of arr[i - 1]) {
      tempArr.push(number + numbers[i]);
      tempArr.push(number - numbers[i]);
    }
    arr.push(tempArr);
  }
  arr[arr.length - 1].forEach((v) => {
    if (v === target) {
      answer++;
    }
  });

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
