import heapq
from collections import defaultdict

def solve():
    with open('z3.2.txt', 'r') as file:
        lines = file.readlines()

    n, k, m = map(int, lines[0].strip().split())

    plans = []
    for idx, line in enumerate(lines[1:m + 1]):
        l, r, c, p = map(int, line.strip().split())
        plans.append((p, l - 1, r - 1, c, idx))

    events = defaultdict(list)
    for p, l, r, c, idx in plans:
        events[l].append(('start', p, c, idx))
        events[r + 1].append(('end', p, c, idx))

    total_cost = 0
    active_plans = {}
    heap = []

    for day in range(n):
        for event in events[day]:
            typ, p, c, idx = event
            if typ == 'start':
                active_plans[idx] = (p, c)
                heapq.heappush(heap, (p, c, idx))
            else:  # end
                if idx in active_plans:
                    del active_plans[idx]

        # Выбираем k самых дешевых ядер
        needed = k
        cost = 0
        temp_heap = []

        while needed > 0 and heap:
            p, c, idx = heapq.heappop(heap)
            if idx not in active_plans:
                continue
            use = min(c, needed)
            cost += use * p
            needed -= use
            temp_heap.append((p, c, idx))

        for item in temp_heap:
            heapq.heappush(heap, item)

        total_cost += cost

    print(total_cost)

solve()
