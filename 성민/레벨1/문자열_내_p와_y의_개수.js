function solution(s) {
  let p = 0;
  let y = 0;
  s.toLowerCase()
    .split("")
    .forEach((v) => {
      if (v === "p") p++;
      else if (v === "y") y++;
    });
  return p === y ? true : false;
}
