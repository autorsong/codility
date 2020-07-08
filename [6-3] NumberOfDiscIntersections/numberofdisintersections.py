def solution(A):
    endpoints = list()

    for origin, radius in enumerate(A):
        endpoints.append((origin - radius, -1))
        endpoints.append((origin + radius, 1))

    endpoints.sort()

    intersections = 0
    inter_counts = 0

    for endpoint in endpoints:
        if endpoint[1] == 1:
            inter_counts -= 1
        elif endpoint[1] == -1:
            intersections += inter_counts
            inter_counts += 1

        if intersections > 10000000:
            return -1

    return intersections
