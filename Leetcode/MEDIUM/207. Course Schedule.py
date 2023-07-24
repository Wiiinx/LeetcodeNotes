def canFinish(numCourses, prerequisites):
    # nums =5, prerequisites= [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    graph = [[] for i in range(numCourses)]
    indeg = [0] * numCourses
    for pre, crs in prerequisites:
        graph[crs].append(pre)
        indeg[pre] += 1

    q = []
    for i in range(numCourses):
        if indeg[i] == 0:  # 不作为prerequisites的课
            q.append(i)


    popNum = 0
    while q:
        # 出队
        crs = q.pop(0)
        popNum += 1

        for pre in graph[crs]:
            indeg[pre] -= 1
            if indeg[pre] == 0:
                q.append(pre)
    return popNum == numCourses






def main():
    print(canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))

    #print(canFinish(2, [[1,0],[0,1]]))

main()