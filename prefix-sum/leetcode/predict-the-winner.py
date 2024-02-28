class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def minimax(turn: int, scores_left: list[int]):
            if len(scores_left) == 1:
                result = [0, scores_left[0]] if turn == 1 else [scores_left[0], 0]
                return result
            if turn == 1:
                right_player1_score = minimax(0, scores_left[: len(scores_left) - 1])
                left_player1_score = minimax(0, scores_left[1:])
                right_choice = scores_left[-1] + right_player1_score[1]
                left_choice = scores_left[0] + left_player1_score[1]
                if right_choice > left_choice:
                    return [right_player1_score[0], right_choice]
                return [left_player1_score[0], left_choice]
            if turn == 0:
                right_player2_score = minimax(1, scores_left[: len(scores_left) - 1])
                left_player2_score = minimax(1, scores_left[1:])
                right_choice = scores_left[-1] + right_player2_score[0]
                left_choice = scores_left[0] + left_player2_score[0]
                if right_choice > left_choice:
                    return [right_choice, right_player2_score[1]]
                return [left_choice, left_player2_score[1]]


        ans = minimax(turn=0, scores_left=nums)
        return ans[0] >= ans[1]