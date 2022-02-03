/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        vector<TreeNode*> curr{root};
        while (!curr.empty()) {
            vector<TreeNode*> temp;
            vector<int> vect;
            for (TreeNode* t : curr) {
                vect.push_back(t->val);
                if (t->left) temp.push_back(t->left);
                if (t->right) temp.push_back(t->right);
            }
            curr = temp;
            res.push_back(vect);
        }
        return res;
    }
};