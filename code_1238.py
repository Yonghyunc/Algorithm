# 1238. [S/W 문제해결 기본] 10일차 - Contact



def calling(s):
    global depth
    depth += 1
    if call[s] != 0 and visited[s] == False:
        visited[s] = True
        # print(visited)
        depth_list[s] = depth
        # print(depth_list)
        for i in range(len(call[s])):
            calling(call[s][i])
            depth = depth_list[s]
    else:
        return depth_list


n, start = map(int, input().split())        # n : 입력받는 문자열의 길이 / start : 시작점
connect = list(map(int, input().split()))

call = [0] * 101

for i in range(n // 2):
    if call[connect[2 * i]] == 0:
        call[connect[2 * i]] = [connect[2 * i + 1]]
    else:
        call[connect[2 * i]].append(connect[2 * i + 1])

print(call)

depth = 0
visited = [False] * 101
depth_list = [0] * 101

calling(start)
print(depth_list)

print(max(depth_list))

# 가장 뒤의 값을 찾기