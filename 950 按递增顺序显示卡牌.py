按递增顺序显示卡牌
class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if deck == None:
            return []
        result = []
        deck = sorted(deck, reverse=True)
        result.append(deck[0])
        for i in range(1, len(deck)):
            result.insert(0, result.pop())
            result.insert(0, deck[i])

        return result
