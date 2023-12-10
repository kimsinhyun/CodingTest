import java.util.*;

// my solution
// runtime 60% memory 7%
class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> vertical = new ArrayList<>();
        List<Set<Character>> horizontal = new ArrayList<>();
        List<Set<Character>> boxes = new ArrayList<>();

        for (int i=0; i<10; i++) {
            vertical.add(new HashSet<Character>());
            horizontal.add(new HashSet<Character>());
            boxes.add(new HashSet<Character>());
        }
        
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                // calculate box
                char c = board[i][j];
                if (c == '.') continue;
                int boxno = (i/3)*3 + (j/3);
                if (horizontal.get(i).contains(c) || vertical.get(j).contains(c) || boxes.get(boxno).contains(c)) return false;
                horizontal.get(i).add(c);
                vertical.get(j).add(c);
                boxes.get(boxno).add(c);

            }
        }

        return true;
    }
}
