class Solution {
public:
    int countVowelStrings(int n) {
        //                 a  e  i  o  u
        //     initially: {1, 1, 1, 1, 1}   
        //       n == 1 : {5, 4, 3, 2, 1}   
        //       n == 2 : {15,10,6, 3, 1}   
        //       n == 3 : {35,20,10,4, 1}   
        
        vector<int> vect{1,1,1,1,1};
        for (int i = 0; i < n; i++) {
            int curr = 1;
            for (int j = 3; j >= 0; j--) {
                curr += vect[j];
                vect[j] = curr;
            }
        }
        return vect[0];
    }
};