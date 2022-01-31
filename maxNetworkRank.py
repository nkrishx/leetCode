def max_network_rank(starts: List[int], ends: List[int], n: int) -> int:
      adj = [0] * (n + 1)

      for a, b in zip(starts, ends):
          adj[a] += 1
          adj[b] += 1

      max_rank = 0

      for a, b in zip(starts, ends):
          max_rank = max(max_rank, adj[a] + adj[b] - 1)

      return max_rank