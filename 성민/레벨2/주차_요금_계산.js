// 처음 180분 5000원 (중복안됨).
// 10분단위 600원 증가.
// 출차 내역이 없으면 23:59 나가는걸로 간주.
// 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
// 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.

function calculateTime(inTime, outTime) {
  let [inHours, inMinutes] = inTime.split(":").map((e) => Number(e));
  let [outHours, outMinutes] = outTime.split(":").map((e) => Number(e));
  if (inMinutes > outMinutes) {
    outHours = outHours - 1;
    outMinutes = outMinutes + 60;
    return (outHours - inHours) * 60 + outMinutes - inMinutes;
  }
  return (outHours - inHours) * 60 + outMinutes - inMinutes;
}

function calculateMoney(
  usedTime,
  default_time,
  default_fee,
  unit_time,
  unit_fee
) {
  let answer = 0;
  if (usedTime <= default_time) return default_fee;
  else {
    answer += default_fee;
    usedTime -= default_time;
    answer += Math.ceil(usedTime / unit_time) * unit_fee;
  }
  return answer;
}

function solution(fees, records) {
  const answer = [];
  const [default_time, default_fee, unit_time, unit_fee] = fees;
  const recordsMap = new Map();
  for (const record of records) {
    const [time, plate, behave] = record.split(" ");
    if (recordsMap.has(plate)) {
      if (behave === "OUT") {
        const [inTime, _, usedTime] = recordsMap.get(plate);
        const newUsedTime = calculateTime(inTime, time);
        recordsMap.set(plate, [time, behave, newUsedTime + usedTime]);
      } else if (behave === "IN") {
        const [inTime, _, usedTime] = recordsMap.get(plate);
        recordsMap.set(plate, [time, behave, usedTime]);
      }
    } else {
      if (behave === "IN") recordsMap.set(plate, [time, behave, 0]);
    }
  }
  for (const recordMap of recordsMap.entries()) {
    if (recordMap[1][1] === "IN") {
      const newUsedTime = calculateTime(recordMap[1][0], "23:59");
      const cost = calculateMoney(
        newUsedTime + recordMap[1][2],
        default_time,
        default_fee,
        unit_time,
        unit_fee
      );
      answer.push([recordMap[0], cost]);
    } else {
      const cost = calculateMoney(
        recordMap[1][2],
        default_time,
        default_fee,
        unit_time,
        unit_fee
      );
      answer.push([recordMap[0], cost]);
    }
  }

  return answer.sort((a, b) => a[0] - b[0]).map((v) => v[1]);
}

solution(
  [180, 5000, 10, 600],
  [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
  ]
);
