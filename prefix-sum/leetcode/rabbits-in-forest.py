class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits_left = defaultdict(int)
        counter = 0
        for i in range(len(answers)):
            counter += 1
            if answers[i] in rabbits_left:
                rabbits_left[answers[i]] -= 1
                if not rabbits_left[answers[i]]:
                    rabbits_left.pop(answers[i])
            elif answers[i] not in rabbits_left and answers[i]:
                rabbits_left[answers[i]] = answers[i]

        for val in rabbits_left.values():
            counter += val

        return counter