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
        Node cur = trie;
        for (int i=0; i<word.length(); i++) {
            char c = word.charAt(i);
            if (!cur.nextChars.containsKey(c)) {
                cur.put(c, new Node());
            } 
            cur = cur.get(c);
        }
        cur.isWord = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, trie);
    }

    private boolean dfs(String word, int cnt, Node cur) {
        if (cnt == word.length()) {
            if (cur.isWord) return true;
            return false;
        }

        char c = word.charAt(cnt);
        if (c == '.') {
            for (char nc: cur.nextChars.keySet()) {
                if(dfs(word, cnt+1, cur.nextChars.get(nc))){
                    return true;
                }
            }
            return false;
        } else if (!cur.nextChars.containsKey(c)) {
            return(dfs(word, cnt+1, cur.nextChars.get(c)));
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */