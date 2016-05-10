#!/usr/bin/env python
# coding=utf-8

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    
    Example 1:
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

"""

import collections

class Solution(object):
    """
    https://leetcode.com/problems/reconstruct-itinerary/

    """


    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = collections.defaultdict(list)

        for start, end in tickets:
            routes[start].append(end)

        def dfs(start):
            left, right = [], []
            for end in sorted(routes[start]):
                if end in routes[start]:
                    routes[start].remove(end)
                    subroutes = dfs(end)

                    if start in subroutes:
                        left += subroutes
                    else:
                        right += subroutes
            return [start] + left + right

        return dfs("JFK")



    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,

        route = []

        def visit(start):
            while targets[start]:
                visit(targets[start].pop())
            route.append(start)

        visit("JFK")
        return route[::-1]


if __name__ =="__main__":
    test = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print test.findItinerary(tickets)
    print test.findItinerary2(tickets)

