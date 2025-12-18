from typing import Optional, List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        INF = 10 ** 18  # "infinity" as int

        min_dist = [INF] * n
        in_mst = [False] * n
        total_cost = 0  # answer to return at the end

        # start at any point
        min_dist[0] = 0

        # iterate through n nodes for Prim's algorithm
        for _ in range(n):
            cost = INF
            prev = -1
            # Step A: Find the cheapest point to connect
            for i in range(n):
                if not in_mst[i] and min_dist[i] < cost:
                    cost = min_dist[i]
                    prev = i

            # Now that we have the cheapest point saved...
            # - Add the cheapest point to the MST
            in_mst[prev] = True

            # - Add the cheapest edge at min_dist[prev] to total_cost
            total_cost += cost

            # - Now that we have the prev point, let's grab the x, y
            prev_x, prev_y = points[prev]

            # Now look through all points and update connection costs for unconnected nodes
            for nex in range(n):
                if not in_mst[nex]:
                    nex_x, nex_y = points[nex]
                    cost = abs(nex_x - prev_x) + abs(nex_y - prev_y)
                    if cost < min_dist[nex]:
                        min_dist[nex] = cost

        return total_cost