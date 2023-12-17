class Trie {
     
    Node root;

    class Node {
        boolean[] alpha;
        boolean[] end;
        Node[] next;

        public Node() {
            alpha = new boolean[26];
            end = new boolean[26];
            next = new Node[26];
        }
    }

    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        int n = word.length();
        Node cur = root;
        
        for (int i=0; i<n; i++) {
            char c = word.charAt(i);
            int index = c - 'a';
            // if alphabet already exists go to next
            if (cur.alpha[index]) {
                if (i == n-1) {
                    cur.end[index] = true;
                }
                cur = cur.next[index]; 
            } else {
                // if doesn't exist, insert
                cur.alpha[index] = true;
                cur.next[index] = new Node();
                if (i == n-1) {
                    cur.end[index] = true;
                }
                cur = cur.next[index];
            } 
        }

    }
    
    public boolean search(String word) {
        int n = word.length();
        Node cur = root;

        for (int i=0; i<n; i++) {
            char c = word.charAt(i);
            int index = c - 'a';
            if (!cur.alpha[index]) {
                return false;
            } else {
                // does exist
                if (i == n-1) {
                    if (!cur.end[index]) return false;
                } 
                cur = cur.next[index];
            }
        } 
        return true;
    }
    
    public boolean startsWith(String prefix) {
        int n = prefix.length();
        Node cur = root;

        for (int i=0; i<n; i++) {
           char c = prefix.charAt(i);
           int index = c - 'a';

            if (!cur.alpha[index]) {
                return false;
            } else {
                cur = cur.next[index];
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */