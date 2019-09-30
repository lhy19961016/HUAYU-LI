def bfsTravel(graph,v0):
    FrontNodes=[v0]
    Travelled=[v0]

    while FrontNodes: #if front node is null, Travelling stops
        next=[]
        for FrontNode in FrontNodes:
            for Current in graph[FrontNode]:
                if Current not in Travelled:
                    Travelled.append(Current)
                    next.append(Current)
        FrontNodes=next
    return Travelled
def dfsTravel(graph, v0):
    travel = []
    stack = [v0]
    while stack:
        Current = stack.pop()
        if Current not in travel:
            travel.append(Current)
        for next_adj in graph[Current]:
            if next_adj not in travel:
                stack.append(next_adj)
    return travel
if __name__ == '__main__':
    graph = {
        '0':['1','2'],
        '1':['0','3','4'],
        '2':['0','6'],
        '3':['1','5'],
        '4':['1','5'],
        '5':['3','4'],
        '6':['2']
    }
    print(bfsTravel(graph, '0')) #Идеальный выход:0 1 2 6 4 3 5/0 1 2 3 4 6 5
    print(dfsTravel(graph,'0'))#Идеальный выход:0 2 6 1 4 5 3
