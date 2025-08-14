# DSA Python Cheat Sheet (Quick & Practical)

A compact, copy‑ready reference for coding interviews and contests. Examples assume Python ≥3.10.

---

## 0) Cheats & Fast I/O

```python
import sys
input = sys.stdin.readline  # faster input
INF = 10**18
```

---

## 1) Core Data Structures

### List

```python
arr = [3, 1, 2]
arr.append(4); arr.extend([5, 6])
arr.insert(1, 9)
x = arr.pop()        # last; arr.pop(i) for index
arr.remove(3)        # first 3
arr.reverse()        # in-place
arr.sort()           # in-place; arr.sort(key=lambda x: ..., reverse=True)
sorted_arr = sorted(arr)
idx = arr.index(9)
```

### Tuple & Unpacking

```python
a, b = 1, 2
a, b = b, a  # swap
```

### Dict (hash map)

```python
d = {"a":1, "b":2}
d.get("c", 0)
d["c"] = d.get("c", 0) + 1
for k, v in d.items():
    ...
```

### Set

```python
s = {1, 2, 3}
s.add(4); s.discard(5)
# ops: s & t, s | t, s - t, s ^ t
```

### deque (queue/stack, O(1) ends)

```python
from collections import deque
q = deque([1, 2])
q.append(3); q.appendleft(0)
q.pop(); q.popleft()
```

### Counter & defaultdict

```python
from collections import Counter, defaultdict
cnt = Counter("abracadabra")
first_idx = defaultdict(lambda: -1)
```

### Heap (min-heap)

```python
import heapq as hq
h = [5, 3, 8]; hq.heapify(h)
hq.heappush(h, 1)
smallest = hq.heappop(h)
# max-heap via negation
hq.heappush(h, -x); -hq.heappop(h)
```

### Bisect (binary search in sorted list)

```python
from bisect import bisect_left, bisect_right, insort
pos = bisect_left([1,2,4,4,5], 4)  # 2
insort(arr, x)  # keep arr sorted
```

### itertools (combos/perms)

```python
from itertools import combinations, permutations, product, accumulate
for c in combinations(range(5), 3): ...
for p in permutations([1,2,3]): ...
for x in product([0,1], repeat=3): ...
pref = list(accumulate([1,2,3,4]))  # [1,3,6,10]
```

---

## 2) Algorithmic Templates

### Binary Search (general on answer)

```python
def bs_first_true(lo, hi, ok):  # [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Two Pointers / Sliding Window (longest subarray with constraint)

```python
def longest_at_most_k_distinct(nums, k):
    from collections import defaultdict
    freq, left, best = defaultdict(int), 0, 0
    for right, x in enumerate(nums):
        freq[x] += 1
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Prefix Sum / Difference Array

```python
# prefix sum
pref = [0]
for x in arr:
    pref.append(pref[-1] + x)
# sum of arr[l:r] = pref[r] - pref[l]

# difference array for range add
n = 10
diff = [0]*(n+1)
diff[l] += val; diff[r] -= val
# restore: for i in range(1,n): diff[i]+=diff[i-1]
```

### Fast GCD / LCM

```python
from math import gcd
def lcm(a, b): return a // gcd(a, b) * b
```

### Sieve of Eratosthenes (primes up to n)

```python
def sieve(n):
    is_p = [True]*(n+1)
    is_p[0:2] = [False, False]
    for p in range(2, int(n**0.5)+1):
        if is_p[p]:
            step = p
            start = p*p
            is_p[start:n+1:step] = [False]*(((n - start)//step) + 1)
    return [i for i,v in enumerate(is_p) if v]
```

### Modular Arithmetic

```python
MOD = 10**9 + 7
pow(a, b, MOD)      # fast pow
inv = pow(a, MOD-2, MOD)  # if MOD is prime
```

---

## 3) Graphs

### Adjacency List + BFS / DFS

```python
from collections import deque, defaultdict

g = defaultdict(list)
# for u,v in edges: g[u].append(v); g[v].append(u) # undirected

def bfs(src):
    dist = {src: 0}; q = deque([src])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def dfs(u, seen=set()):
    if u in seen: return
    seen.add(u)
    for v in g[u]:
        if v not in seen:
            dfs(v, seen)
```

### Topological Sort (DAG)

```python
from collections import deque

def topo_sort(n, edges):
    indeg = [0]*n
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v); indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i]==0])
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v]==0: q.append(v)
    return order  # len(order)==n if DAG
```

### Dijkstra (non-negative weights)

```python
import heapq

def dijkstra(n, g, src):
    # g: list of lists of (v,w)
    dist = [float('inf')]*n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### Union–Find (Disjoint Set Union)

```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.r[a] < self.r[b]: a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]: self.r[a] += 1
        return True
```

---

## 4) Dynamic Programming

### Memoization (top‑down)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def f(i, j):
    # base cases
    # transitions
    return ans
```

### Tabulation (bottom‑up)

```python
# Example: 0/1 Knapsack (value max)
# w[i], v[i], capacity W
n = len(w)
dp = [0]*(W+1)
for i in range(n):
    for c in range(W, w[i]-1, -1):
        dp[c] = max(dp[c], dp[c-w[i]] + v[i])
```

---

## 5) Strings

```python
s = "abaabb"
# frequency
from collections import Counter
Counter(s)
# prefix func (KMP) in O(n)

def prefix_function(s):
    pi = [0]*len(s)
    j = 0
    for i in range(1, len(s)):
        while j and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
```

---

## 6) Geometry Bits

```python
# orientation / cross product
def cross(ax, ay, bx, by):
    return ax*by - ay*bx

# sort by polar angle around origin
pts.sort(key=lambda p: (math.atan2(p[1], p[0]), p))
```

---

## 7) Useful Idioms

```python
# sort by multiple keys
arr.sort(key=lambda x: (x[0], -x[1]))

# enumerate with index
for i, x in enumerate(arr): ...

# flatten
flat = [y for x in mat for y in x]

# clamp
def clamp(x, lo, hi): return max(lo, min(hi, x))

# reading grid
grid = [list(input().strip()) for _ in range(n)]
```

---

## 8) Complexity Nuggets

- `list.append/pop()` end: **O(1) amortized**
- `deque` ends: **O(1)**
- `heap push/pop`: **O(log n)**
- `set/dict` average ops: **O(1)**
- `bisect` search: **O(log n)**
- `sort`: **O(n log n)** (Timsort)

---

## 9) Testing Snippets Fast

```python
def main():
    ...
if __name__ == "__main__":
    main()
```

---

### Tip

Prefer built-ins (`sum`, `min`, `max`, `any`, `all`) and library helpers (`heapq`, `bisect`, `itertools`, `collections`) before reinventing the wheel.

