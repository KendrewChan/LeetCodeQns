/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        map<Node*, Node*> hmap;
        Node* curr = head;
        while (curr) {
            hmap[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        while (curr) {
            hmap[curr]->next = hmap[curr->next];
            hmap[curr]->random = hmap[curr->random];
            curr = curr->next;
        }
        return hmap[head];
    }
};