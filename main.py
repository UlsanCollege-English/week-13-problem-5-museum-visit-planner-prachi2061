from collections import deque
from typing import Iterable, List, Tuple, Dict

def shortest_path(rooms: Iterable[str], doors: Iterable[Tuple[str, str]], start: str, goal: str) -> List[str]:
    room_set = set(rooms)
    if start not in room_set or goal not in room_set:
        return []
    if start == goal:
        return [start]
    adj: Dict[str, List[str]] = {r: [] for r in room_set}
    for a, b in doors:
        if a in room_set and b in room_set:
            adj[a].append(b)
            adj[b].append(a)
    q = deque([start])
    visited = {start}
    parent: Dict[str, str] = {}
    while q:
        u = q.popleft()
        if u == goal:
            break
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    if goal not in visited:
        return []
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
