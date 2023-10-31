def tournamentWinner(competitions, results):
    result = {}

    for i in range(len(competitions)):
        key = competitions[i][0 if results[i] else 1]
        if key not in result:
            result[competitions[i][0 if results[i] else 1]] = 0
        result[competitions[i][0 if results[i] else 1]] += 3
    return max(result, key=result.get)
