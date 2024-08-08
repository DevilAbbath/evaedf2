def promcalc(vels):
    if not vels:
        return 0
    return sum(vels) / len(vels)

def overprompostn(vels):
    prom = promcalc(vels)
    positions = [i for i, vel in enumerate(vels) if vel > prom]
    return positions

def main():
    vel = [
        25, 12, 19, 16, 11, 11, 24, 1,
        14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
        14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
        14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
        10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
        11, 10, 18, 10, 14, 5, 23, 20, 23, 21
    ]
    print(overprompostn(vel))

if __name__ == "__main__":
    main()