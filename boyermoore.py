

""" def rechBoyerMoore(expr: str, seq: str) -> int | None:
    pas = len(seq)
    cursor = pas - 1
    index = None
    done = False
    count =  0
    
    while cursor < len(expr) - 1 and done == False:
        print(cursor, len(expr))
        char = expr[cursor]
        print(expr[:cursor] + f">{expr[cursor]}<" + expr[cursor + 1:])
        if char in seq:
            print(f"Caractere '{char}' trouvé dans la séquence, décalage des caractères pour voir si match.")
            for i in range(pas):
                print(f"{count}: {expr[cursor - i: cursor + i]}, {i}")
                if expr[cursor - i: cursor + i] == seq:
                    done = True
                    index = cursor - i - 1
                    print("found")
        
        cursor = min(cursor + pas, len(expr) - 1)
        count += 1
    
    return index

def main() -> None:
    expr = "les saucisses sont cuites."
    seq = "saucisses"
    index = rechBoyerMoore(expr, seq)
    if index != None:
        print("Séquence trouvée à l'index:", index)
        print(expr[:index] + f">{seq}<" + expr[index + len(seq):]) """

def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''

    # Initialize all occurrence as -1
    badChar = [-1]*256

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # return initialized list
    return badChar


def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print("Pattern occur at shift = {}".format(s))

            ''' 
                Shift the pattern so that the next character in text
                    aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                pattern occurs at the end of text
            '''
            s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
        else:
            '''
            Shift the pattern so that the bad character in text
            aligns with the last occurrence of it in pattern. The
            max function is used to make sure that we get a positive
            shift. We may get a negative shift if the last occurrence
            of bad character in pattern is on the right side of the
            current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])


# Driver program to test above function
def main():
    expr = "les saucisses sont cuites."
    seq = "cuites"
    search(expr, seq)
    
if __name__ == "__main__":
    main()