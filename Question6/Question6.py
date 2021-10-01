#!/bin/python3

def theHackathon(n, m, a, b, f, s, t):
    maxes = [f,s,t]
    employeekeys = {}
    groups = {}
    grouplen = 0
    employeegroupmap = {}

    print("reading requests")
    for _ in range(n):
        ins = input().split()
        employeegroupmap[ins[0]] = int(ins[1])

    for _ in range(m):
        requests = input().split()
        if requests[0] not in employeekeys.keys() and requests[1] not in employeekeys.keys():
            print("creating group")
            employeekeys[requests[0]] = len(groups)
            employeekeys[requests[1]] = len(groups)

            groups[grouplen] = {
                "people": requests,
                1 : 0,
                2 : 0,
                3 : 0,
            }
            groups[grouplen][employeegroupmap[requests[0]]] += 1
            groups[grouplen][employeegroupmap[requests[1]]] += 1
            grouplen += 1
            continue
        elif requests[0] in employeekeys.keys() and requests[1] not in employeekeys.keys():
            print("setting group 1")
            if groups[employeekeys[requests[0]]][employeegroupmap[requests[1]]] >= maxes[employeegroupmap[requests[1]]]:
                continue
            employeekeys[requests[1]] = employeekeys[requests[0]]
            groups[employeekeys[requests[1]]]["people"].append(requests[1])
            groups[employeekeys[requests[1]]][employeegroupmap[requests[1]]] += 1
        elif requests[0] not in employeekeys.keys() and requests[1] in employeekeys.keys():
            print("setting group 2")
            if groups[employeekeys[requests[1]]][employeegroupmap[requests[0]]] >= maxes[employeegroupmap[requests[0]]]:
                continue
            employeekeys[requests[0]] = employeekeys[requests[1]]
            groups[employeekeys[requests[0]]]["people"].append(requests[0])
            groups[employeekeys[requests[0]]][employeegroupmap[requests[0]]] += 1
        if len(groups[employeekeys[requests[0]]]) == b:
            print("returning")
            return sorted(groups[employeekeys[requests[0]]])

    largest_group = []
    for k,v in groups.items():
        if len(v["people"]) > len(largest_group):
            largest_group = v["people"].copy()

    if len(largest_group) < a:
        return "no groups"

    return sorted(largest_group)

if __name__ == '__main__':
    inputdata = input().split()

    n = int(inputdata[0])

    m = int(inputdata[1])

    a = int(inputdata[2])

    b = int(inputdata[3])

    f = int(inputdata[4])

    s = int(inputdata[5])

    t = int(inputdata[6])

    lg = theHackathon(n, m, a, b, f, s, t)
    print(lg)
