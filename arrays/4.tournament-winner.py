"""
Day 2: 5th Dec 2022
Arrays - Easy Problem - 4
https://www.algoexpert.io/questions/tournament-winner

Torunament Winner
"""

#Solution 1 - START
def tournamentWinner(competitions, results):
    """
    Time Complexity : O(N) - N is the number of competetions
    Space Complexity: O(k) - k is the number of teams
    """
    winners = {}
    for index in range(len(results)):
        homeTeam = competitions[index][0]
        awayTeam = competitions[index][1]
        currentWinner = homeTeam if results[index] == 1 else awayTeam
        winners[currentWinner] = winners.get(currentWinner, 0) + 1
    return max(winners, key = lambda team: winners[team])
#Solution 1 - END


#Solution 2 - START
def tournamentWinner(competitions, results):
    """
    Time Complexity : O(N) - N is the number of competetions
    Space Complexity: O(k) - k is the number of teams
    """
    winningTeam = ''
    winners = {winningTeam: 0}
    for index in range(len(results)):
        homeTeam, awayTeam = competitions[index]
        currentScore = results[index]
        
        currentWinningTeam = homeTeam if currentScore == 1 else awayTeam
        winners[currentWinningTeam] = winners.get(currentWinningTeam, 0) + 3
        winningTeam = currentWinningTeam if winners[currentWinningTeam] > winners[winningTeam] else winningTeam
    return winningTeam
#Solution 2 - END

