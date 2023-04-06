#!/usr/bin/python3

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = None
        primes = set(range(2, n+1))
        while primes:
            # Maria's turn
            if winner != "Ben":
                m_pick = None
                for p in sorted(primes):
                    if all(p*i not in primes for i in range(2, n//p+1)):
                        m_pick = p
                        break
                if m_pick is None:
                    winner = "Ben"
                    break
                primes -= set(range(m_pick, n+1, m_pick))
            # Ben's turn
            if winner != "Maria":
                b_pick = None
                for p in sorted(primes):
                    if all(p*i not in primes for i in range(2, n//p+1)):
                        b_pick = p
                        break
                if b_pick is None:
                    winner = "Maria"
                    break
                primes -= set(range(b_pick, n+1, b_pick))
        if winner is not None:
            wins[winner] += 1
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None