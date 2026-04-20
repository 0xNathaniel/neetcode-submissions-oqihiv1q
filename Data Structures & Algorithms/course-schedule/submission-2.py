class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for course, pre in prerequisites:
            prereq[course].append(pre)

            if pre in prereq and course in prereq[pre]:
                return False

        visited = set()
        def check_cycle(crs):
            if prereq[crs] == []:
                return True

            if crs in visited:
                return False
            
            visited.add(crs)

            for pre in prereq[crs]:
                if not check_cycle(pre):
                    return False
            
            visited.remove(crs)
            prereq[crs] = []

            return True


        for i in range(numCourses):
            for n in prereq[i]:
                if not check_cycle(n):
                    return False

        return True 