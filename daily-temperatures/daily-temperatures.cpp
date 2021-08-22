class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> stk;
        vector<int> ans(temperatures.size(), 0);
        stk.push_back(0);
        
        for (int i = 1; i < temperatures.size(); i++) {
            int curr = temperatures[i];
            while (!stk.empty() && curr > temperatures[stk.back()]) {
                ans[stk.back()] = i - stk.back();
                stk.pop_back();
            }
            stk.push_back(i);
        }
        return ans;
    }
};