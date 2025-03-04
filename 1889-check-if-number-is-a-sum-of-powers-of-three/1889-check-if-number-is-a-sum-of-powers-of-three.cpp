class Solution {
public:
    bool checkPowersOfThree(int n) {
        int k = 14;
        while (k >= 0){
            int num = pow(3, k);
            if (n >= num){
                n = n - num;
            }
            k -= 1;
        }
        return (true) ? n == 0 : false;
    }
};