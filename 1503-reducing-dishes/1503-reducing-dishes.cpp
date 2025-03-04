class Solution {
public:
    int maxSatisfaction(vector<int>& sat) {
        int n = sat.size();
        int curr = 0;
        int res = 0;
        sort(sat.begin(), sat.end());
        for (int i = n - 1 ; i >= 0 ; i--){
            curr += sat[i];
            if (curr > 0){
                res += curr;
            }
        }
        return res;
    }
};