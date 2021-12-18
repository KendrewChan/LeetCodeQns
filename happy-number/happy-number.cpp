class Solution {
public:
    int getSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += pow(n % 10, 2.0);
            n /= 10;
        }
        return sum;
    }
    
    bool isHappy(int n) {
        // Floyd's Cycle detection -> Slow & Fast pointer
        int slow = getSum(n);
        int fast = getSum(getSum(n));
        // Once "n = 1" is achieved, it will always maintain this value
        while (slow != fast) {
            slow = getSum(slow);
            fast = getSum(getSum(fast));
        }
        return slow == 1;
    }
};