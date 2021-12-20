/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    vector<int> list;
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        transform(nestedList);
    }
    
    void transform(vector<NestedInteger> &nestedList) {
        while (nestedList.size()) {
            NestedInteger ni = nestedList.back();
            if (ni.isInteger()) list.push_back(ni.getInteger());
            else transform(ni.getList());
            nestedList.pop_back();
        }
    }
    
    int next() {
        int nxt = list.back();
        list.pop_back();
        return nxt;
    }
    
    bool hasNext() {
        return list.size() > 0;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */