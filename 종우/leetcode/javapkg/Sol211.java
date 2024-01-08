class Sol211 {

    class Node {
        Map<Character, Node> nextChars;
        boolean isWord;

        Node() {
            nextChars = new HashMap<>();
        }
    }

    Node trie; 

    public WordDictionary() {
        trie = new Node();
    }
    
    public void addWord(String word) {
        Map<Character, Node> cur = trie.nextChars;
        for (int i=0; i<word.length(); i++) {
            char c = word.charAt(i);
            if (cur.containsKey(c)) {
                cur = cur.get(c).nextChars;
            } else {
                for (int j=i; j < word.length(); j++) {
                    char nc = word.charAt(j);
                    cur.put(nc, new Node());
                    if (j == word.length() - 1) {
                        cur.get(nc).isWord = true;
                    }
                    cur = cur.get(nc).nextChars;
                }
                break;
            } 
        }
    }
    
    public boolean search(String word) {
        return dfs(word, 0, trie);
    }

    private boolean dfs(String word, int cnt, Node cur) {
        if (cnt == word.length()) {
            if (cur.isWord) return true;
            else return false;
        }
        char c = word.charAt(cnt);
        if (c == '.') {
            if (cur.nextChars.size() == 0) {
                return false;
            } else {
                for (char nc: cur.nextChars.keySet()) {
                    if(dfs(word, cnt+1, cur.nextChars.get(nc))){
                        return true;
                    }
                }
                return false;
            }
        } else if (!cur.nextChars.containsKey(c)) {
            return false;
        } else {
            return(dfs(word, cnt+1, cur.nextChars.get(c)));
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */