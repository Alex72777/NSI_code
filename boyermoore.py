

def redBoyerMoore(expr: str, seq: str) -> int:
    pas = len(seq)
    cursor = pas - 1
    index = 0
    done = False
    count =  0
    
    while cursor < len(expr) - 1 or done == False:
        print(cursor, len(expr))
        char = expr[cursor]
        if char in seq:
            for i in range(pas):
                print(f"{count}: {expr[cursor - i: cursor + 1]}, {i}")
                if expr[cursor - i: cursor + 1] == seq:
                    done = True
                    print("found")
        
        cursor = min(cursor + pas, len(expr) - 1)
        count += 1
    
    return index

def main() -> None:
    index = redBoyerMoore("les saucisses sont cuites.", "saucisses")
    
if __name__ == "__main__":
    main()