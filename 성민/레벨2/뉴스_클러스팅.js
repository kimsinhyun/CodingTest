const regex = /[0-9,\W]/g;

function getSet(str) {
  const set = [];
  for (let i = 0; i < str.length - 1; i++) {
    const item = str[i] + str[i + 1];
    if (!item.match(regex)) {
      set.push(item);
    }
  }
  return set;
}

function solution(str1, str2) {
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();
  const A = getSet(str1);
  const B = getSet(str2);
  const set = new Set([...A, ...B]);
  console.log(set.values());
  let union = 0;
  let intersection = 0;

  //같은 원소를 검사해서 많은  쪽은 union에 더하고 적은쪽은 intersection에 더한다.
  set.forEach((item) => {
    const has1 = A.filter((x) => x === item).length;
    const has2 = B.filter((x) => x === item).length;
    union += Math.max(has1, has2);
    intersection += Math.min(has1, has2);
  });
  return union === 0 ? 65536 : Math.floor((intersection / union) * 65536);
}

console.log(solution("aa1+aa2", "AAAA12"));
