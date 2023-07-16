def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t: # contains T that is lower
            cur = stack.pop() # pop the temperature index
            res[cur] = i - cur  # update the temperature
        stack.append(i) # append index of T

    #全部丢进stack，如果找到对应higher的， while stack， 把stack里面都pop走
    #没找到的话就加入res, 默认是0


    return res

def main():
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures([30, 40, 50, 60]))
    print(dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))

main()