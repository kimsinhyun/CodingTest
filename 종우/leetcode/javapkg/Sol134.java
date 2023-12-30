// my solution O(n^2) timeout
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int index = -1;
        int n = gas.length;
        for (int i=0; i<n; i++) {
            if (gas[i] >= cost[i]) {
                int rem = gas[i] - cost[i]; 
                boolean reachable = true;
                for (int j=1; j<n; j++) {
                    int k = (i + j) % n;
                    rem += gas[k];
                    if (rem < cost[k]) {
                        reachable = false;
                        break;
                    } 
                    rem -= cost[k];
                }
                if (reachable) return i;
            }
        }
        return index;
    }
}

// Solution after neetcode explanation O(n), but only beats 5%
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length; 
        int sumGas = Arrays.stream(gas).sum();
        int sumCost = Arrays.stream(cost).sum();

        if (sumGas < sumCost) {
            return -1;
        }

        int rem = 0;
        int index = 0;
        for (int i=0; i<n; i++) {
            rem += gas[i] - cost[i];
            if (rem < 0) {
               rem = 0;
               index = i+1;
            } 
        }
        return index;
    }
}