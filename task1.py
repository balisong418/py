def analys_hour():
    hour = input()
    if (hour <= 18) & (hour >= 9):
        return "Im at work"
    else:
        return "Im at home"

if __name__ == "__main__":
    print analys_hour()
