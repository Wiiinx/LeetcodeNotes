# TWO POINTERS
def maxArea1(height):
    left, right, cur_max = 0, len(height) - 1, 0
    while left < right:  # 两边同时 narrow down the container from widest
        cur_max = max(cur_max, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return cur_max


def main():
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]
    height3 = [4, 5, 7, 2, 3, 5, 3, 1, 2]
    print(maxArea1(height1))
    print(maxArea1(height2))
    print(maxArea1(height3))


main()