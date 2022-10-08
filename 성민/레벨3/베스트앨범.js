// 장르 별로 정렬
// 장르 별 많이 재생된 노래 정렬
// 각 장르에서 앞에 두개씩만 추출

function solution(genres, plays) {
  const genreMap = new Map();
  genres.forEach((genre, index) => {
    const curr = genreMap.get(genre) || { total: 0, playList: [] };
    genreMap.set(genre, {
      total: curr.total + plays[index],
      playList: [...curr.playList, [plays[index], index]]
        .sort((a, b) => b[0] - a[0])
        .slice(0, 2),
    });
  });
  return [...genreMap]
    .sort((a, b) => b[1].total - a[1].total)
    .flatMap((x) => x[1].playList)
    .map((x) => x[1]);
}

console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);
