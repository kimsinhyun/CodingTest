function solution(survey, choices) {
  var answer = "";
  const choice_value = {
    1: 3,
    2: 2,
    3: 1,
    4: 0,
    5: 1,
    6: 2,
    7: 3,
  };
  const survey_types = new Map([
    ["R", 0],
    ["T", 0],
    ["C", 0],
    ["F", 0],
    ["J", 0],
    ["M", 0],
    ["A", 0],
    ["N", 0],
  ]);
  let index = -1;
  for (const value of survey) {
    index++;
    if (choices[index] === 4) continue;
    if (choices[index] > 4) {
      const curValue = survey_types.get(value[1]);
      survey_types.set(value[1], choice_value[choices[index]] + curValue);
    } else {
      const curValue = survey_types.get(value[0]);
      survey_types.set(value[0], choice_value[choices[index]] + curValue);
    }
  }
  answer += survey_types.get("R") < survey_types.get("T") ? "T" : "R";
  answer += survey_types.get("C") < survey_types.get("F") ? "F" : "C";
  answer += survey_types.get("J") < survey_types.get("M") ? "M" : "J";
  answer += survey_types.get("A") < survey_types.get("N") ? "N" : "A";
  return answer;
}

console.log(solution(["TR", "RT", "TR"], [7, 1, 3]));
