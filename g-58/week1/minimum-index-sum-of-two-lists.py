class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = defaultdict(list)
        set1,set2 = set(list1),set(list2)
        intersection = set1.intersection(set2)
        for word in intersection:
            indices[word].append(list1.index(word))
            indices[word].append(list2.index(word))
        min_sum = min([sum(ls) for ls in indices.values()])
        return [word for word in indices if sum(indices[word])==min_sum]