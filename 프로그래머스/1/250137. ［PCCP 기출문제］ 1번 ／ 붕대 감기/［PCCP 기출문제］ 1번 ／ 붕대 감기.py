def solution(bandage, health, attacks):
    end_time = attacks[-1][0]
    attack_idx = 0
    max_health = health
    streak = 0
    
    for i in range(1, end_time+1):
        if i == attacks[attack_idx][0]: 
            health -= attacks[attack_idx][1]
            streak = 0
            attack_idx += 1
            if health <= 0: return -1
        else:
            streak += 1
            health += bandage[1]
            if streak >= bandage[0]:
                health += bandage[2]
                streak = 0
            if health >= max_health:
                health = max_health
 
    if health > 0: return health
    return -1