class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for i,j in paths:
            cities[i] = j
        fr = list(cities.keys())
        for dest in cities.values():
            if dest not in fr:
                return dest
