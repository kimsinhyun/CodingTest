// function solution(s) {
//     let answer = '';
//     s=s.toLowerCase().split('');
//     let inStr=0;
//     for(let i=0;i<s.length;){
//         if(s[i]===" "){
//             while(s[i]===" "){
//                 answer+=s[i];
//                 i++;
//             }
//             inStr=0;
//         }else if(isNaN(s[i]) && !inStr){
//             answer+=s[i].toUpperCase();
//             inStr=1;
//             i++;
//         }else{
//             answer+=s[i];
//             inStr=1;
//             i++;
//         }
//     }
//     return answer;
// }

function solution(s) {
  var answer = "";
  let isSpace = true;
  for (const word of s.split("")) {
    if (word !== " " && isSpace) {
      answer += word.toUpperCase();
      isSpace = false;
    } else if (word !== " " && !isSpace) {
      answer += word.toLowerCase();
    } else if (word === " ") {
      answer += word;
      isSpace = true;
    }
  }
  return answer;
  // 뱐걍
}
