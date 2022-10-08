function solution(id_list, report, k) {
  const result = [];
  const reporterMap = new Map([]);
  const reportedMap = new Map([]);
  for (const id of id_list) {
    reporterMap.set(id, []);
    reportedMap.set(id, []);
  }

  for (const r of report) {
    const [reporter, reported] = r.split(" ");
    const reporterArray = reporterMap.get(reporter);
    const reportedArray = reportedMap.get(reported);
    if (reporterArray.includes(reported)) continue;
    reporterArray.push(reported);
    reportedArray.push(reporter);
    reporterMap.set(reporter, reporterArray);
    reportedMap.set(reported, reportedArray);
  }

  const blockUsers = [...reportedMap.entries()]
    .filter((v) => !(v[1].length < k))
    .map((v) => v[0]);

  for (const v of reporterMap.values()) {
    let sendMailCnt = 0;
    for (const r of blockUsers) {
      if (v.includes(r)) sendMailCnt++;
    }
    result.push(sendMailCnt);
  }
  return result;
}

solution(
  ["muzi", "frodo", "apeach", "neo"],
  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
  2
);
