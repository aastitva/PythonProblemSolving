def maxArea(heights):
    L = 0
    R = len(heights) - 1
    max_area = 0
    while L < R:
        max_area = max(max_area, min(heights[L], heights[R]) * (R - L))
        if heights[L] < heights[R]:
            L += 1
        else:
            R -= 1
    return max_area