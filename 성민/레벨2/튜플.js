function solution(s) {
  const regex = /{/g;
  const answer = new Set();

  const str = s
    .replace(regex, "")
    .split("},")
    .map((item) => {
      if (item.includes("}}")) {
        return item.replace("}}", "");
      }
      return item;
    })
    .sort((a, b) => a.length - b.length);

  for (const item of str) {
    const items = item.split(",").map((v) => Number(v));
    for (const i of items) {
      if (answer.has(i)) continue;
      else {
        answer.add(i);
        break;
      }
    }
  }

  return Array.from(answer.values());
}
