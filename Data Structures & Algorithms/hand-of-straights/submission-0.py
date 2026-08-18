class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num] >0 :
                # print(count[num])
                # print(num)
                for i in range(num, num + groupSize):

                    if not count[i]:
                        return False
                    
                    count[i] -=1

                # print(count)


        return True

        