def solution(tickets):
    ticket_dict = {}
    n = len(tickets) + 1
    for start, dest in tickets:
        if start in ticket_dict: 
            if dest not in ticket_dict[start]: 
                ticket_dict[start][dest] = 1
            else:
                ticket_dict[start][dest] = ticket_dict[start][dest] + 1 
        else: 
            ticket_dict[start] = {dest: 1}
    s = ["ICN"]
    dupl_check = set()
    
    def dfs(n, ticket_dict):
        last = s[-1]
        if len(s) == n: return
        while len(s) < n:

            if last in ticket_dict:
                for i in sorted(ticket_dict[last]):
                    if ticket_dict[last][i] == 0: continue
                    s.append(i)
                    ticket_dict[last][i] -= 1
                    if ' '.join(s) not in dupl_check: 
                        dfs(n, ticket_dict)
                        if len(s) == n: return 
                        dupl_check.add(' '.join(s))
                        ticket_dict[last][i] += 1
                        s.pop()
                    else:
                        ticket_dict[last][i] += 1
                        s.pop()
                        return          

            else:
                return

    dfs(n, ticket_dict)
    return s
