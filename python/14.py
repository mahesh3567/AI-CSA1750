import math
MAX, MIN = float('inf'), float('-inf')
def minimax(depth, nodeIndex, treeDepth, maximizingPlayer, values, alpha, beta):
    if depth == treeDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(2):  
            val = minimax(depth + 1, nodeIndex * 2 + i, treeDepth, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, treeDepth, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    treeDepth = int(math.log(len(values), 2)) 
    print("The optimal value is:", minimax(0, 0, treeDepth, True, values, MIN, MAX))