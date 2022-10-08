function solution(s) {
  const numberList = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  let str = s;
  numberList.forEach((v, index) => {
    while (str.includes(v)) {
      str = str.replace(v, index);
    }
  });
  return Number(str);
}
