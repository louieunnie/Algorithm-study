
customers = [("A",5,"X"),("B",4,"Y"),("C",5,"Y")]


def best_region(customers: list[tuple[str, int, str]]) -> list[str]:
    data = {}
    for x in customers:
        customer, rate, region = x
        if region in data:
            data[region].append(rate)
        else:
            data[region] = [rate]
    maximum = 0
    largest = []
    for d in data:
        avg = sum(data[d])/len(data[d])
        data[d] = avg
        if maximum < avg:
            maximum = avg
            largest = [d]
        elif maximum == avg:
            largest.append(d)
    return sorted(largest)

print(best_region(customers))
# Output: ['Busan']