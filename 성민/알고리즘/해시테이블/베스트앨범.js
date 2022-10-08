function getGenresLank(map) {
  const answer = [];
  for (const v of map) {
    const [genre, playsCnt] = v;
    const total = playsCnt.reduce((pre, cur) => [pre[0] + cur[0], 0], [0, 0]);
    answer.push([genre, total[0]]);
  }
  return answer.sort((a, b) => b[1] - a[1]).map((v) => v[0]);
}

function solution(genres, plays) {
  var answer = [];
  const map = new Map();
  for (let i = 0; i < plays.length; i++) {
    const genre = genres[i];
    const playCnt = plays[i];
    if (map.get(genre) === undefined) {
      map.set(genre, [[playCnt, i]]);
    } else {
      const genrePlayList = map.get(genre);
      genrePlayList.push([playCnt, i]);
      map.set(genre, genrePlayList);
    }
  }
  const genresLank = getGenresLank(map);
  for (const v of genresLank) {
    answer.push(
      ...map
        .get(v)
        .sort((a, b) => b[0] - a[0])
        .slice(0, 2)
        .map((m) => m[1])
    );
  }
  return answer;
}
