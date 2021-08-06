/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> sol;
        if (root == NULL) return sol;
        vector<Node*> vect;
        vect.push_back(root);
        while (vect.size() > 0) {
            vector<Node*> nxt;
            vector<int> temp;
            for (Node* curr : vect) {
                temp.push_back(curr->val);
                for (Node* child : curr->children) {
                    nxt.push_back(child);
                }
            }
            sol.push_back(temp);
            vect = nxt;
        }
        return sol;
    }
};