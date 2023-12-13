import java.util.*;
class Sol3 {
    public int lengthOfLongestSubstring(String s) {
        int l = 0, r = 0;
        int len = 0;
        Set<Character> seen = new HashSet<>();
        while (r < s.length()) {
            char c = s.charAt(r);
            System.out.println(c);
            if (seen.contains(c)){
                len = Math.max(len, r-l);
                while(l<r) {
                    char h = s.charAt(l);
                    l++;
                    seen.remove(h);
                    if (c == h) {
                        break;
                    }
                }
                
            }
            seen.add(c);
            r++;
        }        
        System.out.println(r + " " + l);
        len = Math.max(len, r-l); 
        return len;
    }
}