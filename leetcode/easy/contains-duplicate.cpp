#include<set>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int>my_set;
        for(auto i:nums){
            my_set.insert(i);
        } 
        if (my_set.size()== nums.size()){
            return false;
        }
        else{
            return true;
        }
    }
};
