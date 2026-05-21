Design and Analysis of Algorithms Lab (PCS409)
University: Graphic Era Hill University
Semester: IV · B.Tech CSE (AI & ML) 
Language: Python


Table of Contents
Week
Topic
Week 1
Searching — Linear, Binary, Jump
Week 2
Advanced Searching — First/Last Occurrence, Count Pairs
Week 3
Sorting — Insertion, Selection
Week 4
Divide & Conquer — Merge Sort, Quick Sort
Week 5
Greedy Basics — Two Sum
Week 6
Graph Traversal — DFS Path
Week 7
Shortest Path — Dijkstra, Bellman-Ford
Week 8
Minimum Spanning Tree — Prim's
Week 9
Greedy — Fractional Knapsack
Week 11
Dynamic Programming I — Coin Change, Subset Sum
Week 12
Dynamic Programming II — LCS
Week 13
Hashing — Duplicate in Window
Week 14
DP / Graph — Ugly Number, Mother Vertex



Format
Each implementation follows a consistent structure:

Core function
Check / validation function (where applicable)
Driver code
How it works
Time & Space complexity


Week 1 — Searching
Linear Search
def linear_search(arr, key):

    comparisons = 0

    for i in range(len(arr)):

        comparisons += 1

        if arr[i] == key:

            return True, comparisons

    return False, comparisons


def check(arr, n):

    print("Okay" if len(arr) == n else "Size mismatch")


t = int(input())

while t:

    n = int(input())

    arr = list(map(int, input().split()))

    check(arr, n)

    key = int(input())

    found, c = linear_search(arr, key)

    print("Present" if found else "Not Present", c)

    t -= 1

How it works: Scans each element sequentially until the key is found. Time: O(n) · Space: O(1)


Binary Search
def binary_search(arr, key):

    low, high = 0, len(arr) - 1

    comparisons = 0

    while low <= high:

        mid = (low + high) // 2

        comparisons += 1

        if arr[mid] == key:

            return True, comparisons

        elif key < arr[mid]:

            high = mid - 1

        else:

            low = mid + 1

    return False, comparisons

How it works: Repeatedly halves the search space on a sorted array. Time: O(log n) · Space: O(1)


Jump Search
import math

def jump_search(arr, key):

    n = len(arr)

    step = int(math.sqrt(n))

    prev = 0

    while prev < n and arr[min(step, n) - 1] < key:

        prev = step

        step += int(math.sqrt(n))

        if prev >= n:

            return False

    for i in range(prev, min(step, n)):

        if arr[i] == key:

            return True

    return False

How it works: Jumps ahead by √n steps, then performs linear search in the identified block. Time: O(√n) · Space: O(1)


Week 2 — Advanced Searching
First & Last Occurrence
def first_occ(arr, key):

    l, h, res = 0, len(arr) - 1, -1

    while l <= h:

        m = (l + h) // 2

        if arr[m] == key:

            res = m

            h = m - 1

        elif arr[m] < key:

            l = m + 1

        else:

            h = m - 1

    return res

How it works: Modified binary search that continues left after finding the key to locate the first occurrence. Time: O(log n) · Space: O(1)


Count Pairs with Difference K
def count_pairs(arr, k):

    arr.sort()

    count = 0

    for i in range(len(arr)):

        target = arr[i] + k

        l, h = i + 1, len(arr) - 1

        while l <= h:

            m = (l + h) // 2

            if arr[m] == target:

                count += 1

                break

            elif arr[m] < target:

                l = m + 1

            else:

                h = m - 1

    return count

How it works: For each element, binary searches for element + k in the remaining array. Time: O(n log n) · Space: O(1)


Week 3 — Sorting
Insertion Sort
def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr

How it works: Builds the sorted array one element at a time by inserting each into its correct position. Time: O(n²) · Space: O(1)


Selection Sort
def selection_sort(arr):

    for i in range(len(arr)):

        min_i = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_i]:

                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr

How it works: Repeatedly selects the minimum from the unsorted portion and places it at the front. Time: O(n²) · Space: O(1)


Week 4 — Divide & Conquer
Merge Sort
def merge_sort(arr):

    if len(arr) <= 1:

        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(l, r):

    res = []

    i = j = 0

    while i < len(l) and j < len(r):

        if l[i] < r[j]:

            res.append(l[i])

            i += 1

        else:

            res.append(r[j])

            j += 1

    res += l[i:]

    res += r[j:]

    return res

How it works: Recursively splits the array in half, sorts each half, then merges them back. Time: O(n log n) · Space: O(n)


Quick Sort
def quick_sort(arr):

    if len(arr) <= 1:

        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]

    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

How it works: Partitions the array around a pivot, then recursively sorts each partition. Time: O(n log n) average, O(n²) worst · Space: O(log n)


Week 5 — Greedy Basics
Two Sum
def two_sum(arr, k):

    arr.sort()

    l, r = 0, len(arr) - 1

    while l < r:

        s = arr[l] + arr[r]

        if s == k:

            return arr[l], arr[r]

        elif s < k:

            l += 1

        else:

            r -= 1

    return None

How it works: Two-pointer approach on a sorted array — converge pointers based on the current sum. Time: O(n log n) · Space: O(1)


Week 6 — Graph Traversal
DFS Path
def dfs(graph, src, dest, vis):

    if src == dest:

        return True

    vis[src] = True

    for i in range(len(graph)):

        if graph[src][i] == 1 and not vis[i]:

            if dfs(graph, i, dest, vis):

                return True

    return False

How it works: Depth-first traversal from source; returns True if destination is reachable. Time: O(V + E) · Space: O(V)


Week 7 — Shortest Path
Dijkstra's Algorithm
import heapq

def dijkstra(graph, src):

    n = len(graph)

    dist = [float('inf')] * n

    dist[src] = 0

    pq = [(0, src)]

    while pq:

        d, u = heapq.heappop(pq)

        for v in range(n):

            if graph[u][v] != 0:

                nd = d + graph[u][v]

                if nd < dist[v]:

                    dist[v] = nd

                    heapq.heappush(pq, (nd, v))

    return dist

How it works: Greedy shortest-path using a min-heap; works on non-negative weighted graphs. Time: O((V + E) log V) · Space: O(V)


Bellman-Ford Algorithm
def bellman_ford(edges, n, src):

    dist = [float('inf')] * n

    dist[src] = 0

    for _ in range(n - 1):

        for u, v, w in edges:

            if dist[u] + w < dist[v]:

                dist[v] = dist[u] + w

    return dist

How it works: Relaxes all edges n−1 times; handles negative weights. Time: O(VE) · Space: O(V)


Week 8 — Minimum Spanning Tree
Prim's Algorithm
def prim(graph):

    n = len(graph)

    selected = [False] * n

    selected[0] = True

    cost = 0

    for _ in range(n - 1):

        m = float('inf')

        x = y = 0

        for i in range(n):

            if selected[i]:

                for j in range(n):

                    if not selected[j] and graph[i][j]:

                        if graph[i][j] < m:

                            m = graph[i][j]

                            x, y = i, j

        cost += m

        selected[y] = True

    return cost

How it works: Grows the MST one edge at a time by always picking the minimum-weight edge connecting the tree to an unvisited vertex. Time: O(V²) · Space: O(V)


Week 9 — Greedy
Fractional Knapsack
def knapsack(w, v, W):

    items = sorted(

        [(v[i] / w[i], w[i], v[i]) for i in range(len(w))],

        reverse=True

    )

    total = 0

    for r, wt, val in items:

        if W >= wt:

            total += val

            W -= wt

        else:

            total += r * W

            break

    return total

How it works: Sorts items by value/weight ratio; greedily fills the knapsack, taking fractions when needed. Time: O(n log n) · Space: O(n)


Week 11 — Dynamic Programming I
Coin Change (Count Ways)
def coin_change(coins, target):

    dp = [0] * (target + 1)

    dp[0] = 1

    for c in coins:

        for i in range(c, target + 1):

            dp[i] += dp[i - c]

    return dp[target]

How it works: Bottom-up DP; dp[i] stores the number of ways to make amount i. Time: O(n × target) · Space: O(target)


Subset Sum (Equal Partition)
def subset(arr):

    s = sum(arr)

    if s % 2:

        return False

    target = s // 2

    dp = [False] * (target + 1)

    dp[0] = True

    for num in arr:

        for j in range(target, num - 1, -1):

            dp[j] = dp[j] or dp[j - num]

    return dp[target]

How it works: Checks if array can be split into two equal-sum subsets using 1D DP. Time: O(n × target) · Space: O(target)


Week 12 — Dynamic Programming II
Longest Common Subsequence (LCS)
def lcs(a, b):

    m, n = len(a), len(b)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

How it works: Fills an (m+1)×(n+1) table; dp[i][j] is the LCS length of a[:i] and b[:j]. Time: O(mn) · Space: O(mn)


Week 13 — Hashing
Duplicate in Window of Size K
def dup_window(arr, k):

    s = set()

    for i in range(len(arr)):

        if arr[i] in s:

            return True

        s.add(arr[i])

        if len(s) > k:

            s.remove(arr[i - k])

    return False

How it works: Maintains a sliding window of size k using a set; returns True if any duplicate exists within the window. Time: O(n) · Space: O(k)


Week 14 — DP / Graph
Nth Ugly Number
def ugly(n):

    u = [1] * n

    i2 = i3 = i5 = 0

    for i in range(1, n):

        u[i] = min(u[i2] * 2, u[i3] * 3, u[i5] * 5)

        if u[i] == u[i2] * 2: i2 += 1

        if u[i] == u[i3] * 3: i3 += 1

        if u[i] == u[i5] * 5: i5 += 1

    return u[-1]

How it works: Generates ugly numbers in order using three pointers for multiples of 2, 3, and 5. Time: O(n) · Space: O(n)


Mother Vertex in a Graph
def dfs(graph, v, vis):

    vis[v] = True

    for i in range(len(graph)):

        if graph[v][i] == 1 and not vis[i]:

            dfs(graph, i, vis)


def mother(graph):

    n = len(graph)

    vis = [False] * n

    last = 0

    for i in range(n):

        if not vis[i]:

            dfs(graph, i, vis)

            last = i

    vis = [False] * n

    dfs(graph, last, vis)

    return last if all(vis) else -1

How it works: Uses Kosaraju's idea — the last vertex to finish DFS on the full graph is a candidate; verify by checking if it can reach all other vertices. Time: O(V + E) · Space: O(V)
