A = [8,7,3,5,2,1]
sum = 10

def PairOfTwoNumber(A,sum):
    # here taking the range for loop of range end of the A list element
    for i in range(len(A) - 1):
        # here taking the range for the loop start at increament and check the length of a start to end
        for j in range(i+1, len(A)):
            # here both the range of for loop equal to its sums comes
            if A[i] + A[j] == sum:
                print("Pair is found", (A[i],A[j]))
                return
    print("Pair is not found")

PairOfTwoNumber(A,sum)