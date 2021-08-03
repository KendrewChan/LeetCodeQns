class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> lettersVect;
        lettersVect.push_back("abc");
        lettersVect.push_back("def");
        lettersVect.push_back("ghi");
        lettersVect.push_back("jkl");
        lettersVect.push_back("mno");
        lettersVect.push_back("pqrs");
        lettersVect.push_back("tuv");
        lettersVect.push_back("wxyz");
        
        vector<string> vect;
        for (int i = 0; i < digits.length(); i++) {
            int idx = int(digits[i]-'0')-2;
            string letters = lettersVect[idx];
            if (i == 0) {
                for (int z = 0; z < letters.length(); z++) {
                    string s = "";
                    vect.push_back(s + letters[z]);
                }
            } else {
                vector<string> temp;
                for (int j = 0; j < vect.size(); j++) {
                    for (int z = 0; z < letters.length(); z++) {
                        string s = vect[j] + letters[z];
                        temp.push_back(s);
                    }
                }
                vect = temp;
            }
        }
   
        return vect;
    }
};