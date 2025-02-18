def(a,b):
return 0
def nemeh(a: float, b: float) -> float:
    return a + b


def hasah(a: float, b: float) -> float:
    return a - b


if __name__ == "__main__":
    num1 = float(input("1: "))
    num2 = float(input("2: "))

    print(f"niilber: {nemeh(num1, num2)}")
    print(f"ylgaa: {hasah(num1, num2)}")

