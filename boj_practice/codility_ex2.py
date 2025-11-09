# import math
records = [
    ("Seoul", "2025-11-01", 13.2),
    ("Seoul", "2025-11-02", 12.8),
    ("Seoul", "2025-11-03", 27.5),   # ⬅️ 훨씬 높은 온도 (이상치)
    ("Busan", "2025-11-01", 16.5),
    ("Busan", "2025-11-02", 16.8),
    ("Busan", "2025-11-03", 24.5),   # ⬅️ 이상치
]


# def far_from_std(value, mean):


def find_anomalies(records: list[tuple[str, str, float]]) -> list[tuple[str, str]]: 
    """
    Return a list of (city, date) pairs where the temperature is an anomaly.
    Output list should be sorted first by city name, then by date (ascending).
    """
    data = {}
    ans = []
    for r in records:
        city, date, temp = r
        if city in data:
            data[city].append((date, temp))
        else:
            data[city] = [(date, temp)]
    for d in data:
        avg = sum([x[1] for x in data[d]])/len(data[d])
        var = sum([(x[1]-avg)**2 for x in data[d]])/len(data[d])
        std = var ** 0.5
        print(avg)
        print(var)
        print(2*std)
        print(avg-2*std)
        print(avg+2*std)
        for x in data[d]:
            print(x)
            if avg-2*std > x[1] or avg + 2*std < x[1]:
                ans.append((d, x[0]))
    return ans
print(find_anomalies(records))

# Output: [('Busan', '2025-11-03'), ('Seoul', '2025-11-03')]
