class Test(object):
    def networkDelayTime(self, times, N, K):
        graph = {}      #Построить графику
        for u, v, w in times:
            graph[u] = graph.get(u, {})
            graph[u][v] = w

        if K not in graph:
            return -1

        dists = [graph[K].get(i, float('inf')) for i in range(1, N + 1)]

        otherspoint = list(range(1, K)) + list(range(K + 1, N + 1))

        while otherspoint:
            mini = float('inf')
            _idx = 0
            _point = 0

            for idx, point in enumerate(otherspoint):
                if dists[point-1] < mini:
                    mini, _idx, _point = dists[point-1], idx, point
            otherspoint.pop(_idx)

            if _point in graph:
                for v, w in graph[_point].items():
                    if dists[v-1] > w + mini:
                        dists[v-1] = w + mini
        dists.pop(K-1)
        time = max(dists)
        if time == float('inf'):
            return -1
        return time
if __name__ == "__main__":
    Net = Test()
    print("How long:", Net.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2))
