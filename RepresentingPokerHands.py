import enum 
class Rank(enum.Enum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10
 
def evaluate(hand):
    suits = []
    ranks = []
    # split hand into ranks and suits
    count = 0
    for i in hand:
        if count % 2 == 0:
            ranks.append(i)
        else:
            suits.append(i)
        count += 1

    # the most common rank
    most_common = max(ranks, key=ranks.count)

    # check for four of a kind
    if ranks.count (most_common) == 4:
        return "four of a kind"

    # the most common suit
    common_suit= max(suits, key=suits.count) 

    # check for flush
    if suits.count(common_suit) == 5:
        return "flush"
    
    # check for three of a kind
    if ranks.count(most_common) == 3:
        ranks2 = []
        for c in ranks :
            if c!= most_common :
                ranks2.append(c)
        if ranks2[0] == ranks2[1] :
            return "full house"
        else:
            return "three of a kind"
        
    # check for pair
    if ranks.count(most_common) == 2:
        return "pair"

    # check for high card
    if not ranks[0].isdigit():
        highest_rank = Rank[ranks[0]].value
    else:
        highest_rank = int(ranks[0])
    for r in ranks:
        if not r.isdigit():
            curr = Rank[r].value
        else:
            curr = int(r)
            
        if curr > highest_rank:
            highest_rank = curr


    return Rank(highest_rank).name + " high"
        
    

print("KcKdKhKs4c evaluates to: ", evaluate("KcKdKhKs4c"))

print("2s3s8s9sKs evaluates to: ", evaluate("2s3s8s9sKs"))

print("KcKhKsTcTs evaluates to: ", evaluate("KcKhKsTcTs"))

print("KcKhKsTc9s evaluates to: ", evaluate("KcKhKsTc9s"))

print("KcQhKsTc9s evaluates to: ", evaluate("KcQhKsTc9s"))

print("KcQh8sTc9s evaluates to: ", evaluate("KcQh8sTc9s"))

print("2cQh8sTc9s evaluates to: ", evaluate("2cQh8sTc9s"))

