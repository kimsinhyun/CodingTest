import java.util.Arrays;
//https://leetcode.com/problems/valid-anagram/

class Sol242 {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] sch = s.toCharArray();
        char[] tch = t.toCharArray();

        Arrays.sort(sch);
        Arrays.sort(tch);

        for (int i=0; i<sch.length; i++) {
            if (sch[i] != tch[i]) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        Sol242 Driver = new Sol242();

        System.out.println(Driver.isAnagram(s, t));
    }
}