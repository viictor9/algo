import random 

def hiring():
    candidates = []
    num = int(input("Enter num of candidates: "))
    for i in range(num):
        name = input(f"Enter the name {i+1}: ")
        iq = int(input(f"Enter the iq {i+1}: "))
        candidates.append((name, iq))

    return candidates


if __name__ == "__main__":
    candidates = hiring()


random.shuffle(candidates)
candidates.sort(key=lambda x: x[1], reverse=True)

if candidates:
    highest = candidates[0]
    print("the selected candidate is " + highest[0])

else:
    print("no candidate selected")
