class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        int res = 0;
        unordered_set<int> lookup(arr.begin(), arr.end()); 
        for (int i = 0 ; i < n ; i++){
            for (int j = i + 1 ; j < n ; j++){
                int curr = 2;
                int n1 = arr[i];
                int n2 = arr[j];
                while (lookup.find(n1 + n2) != lookup.end()){
                    auto temp = n1;
                    n1 = n2;
                    n2 = n2 + temp;
                    curr = curr + 1;
                }
            if (res < curr){
                res = curr;
            }
            }

        }
        return (res >= 3) ? res : 0;
    }
};
