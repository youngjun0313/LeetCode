public class Solution {
    public static void main(String[] args) {
        System.out.println(isMatch("bbbba", ".*a*a"));
    }

    public static boolean isMatch(String s, String p) {
        int pPivot = 0;
        int sPivot = 0;
        int m = p.length();
        int n = s.length();
        while(sPivot<n && pPivot<m) {
            char c = s.charAt(sPivot);
            char pattern = p.charAt(pPivot);
            System.out.println(c);
            System.out.println(pattern);
            if(pPivot+1<m && p.charAt(pPivot+1)=='*') {
                if(pattern == '.' || pattern == c)
                    sPivot++;
                else
                    pPivot+=2;
            } else if(pattern == '.' || pattern == c) {
                sPivot++;
                pPivot++;
            } else
                return false;
        }
        if(sPivot==n) {
            if(pPivot == m)
                return true;
            else if (pPivot+1>=m)
                return false;
            else if (p.charAt(pPivot+1) != '*')
                return false;
            else {
                char prev = p.charAt(pPivot);
                pPivot+=2;
                while(pPivot<m) {
                    if(pPivot+1<m && p.charAt(pPivot)=='*')
                        pPivot++;
                    else if(p.charAt(pPivot) != prev)
                        return false;
                    else
                        pPivot++;
                }
                return true;
            }

        } else
            return false;
    }
}
