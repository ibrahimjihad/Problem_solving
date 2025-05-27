"""
Problem: Compare the Triplets
Category: Implementation
Platform: HackerRank

Description:
Alice and Bob each created a list of three integers to represent their ratings in three categories: problem clarity, originality, and difficulty.
You must compare their ratings and award points:
- If Alice's rating in a category is higher than Bob's, she receives 1 point.
- If Bob's rating in a category is higher than Alice's, he receives 1 point.
- If they are equal, neither gets a point.

Return the result as a list of two integers: [Alice's score, Bob's score].

Example:
Input: a = [5, 6, 7], b = [3, 6, 10]
Output: [1, 1]
"""

def compare_triplets(a, b):
    score = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
    return score

if __name__ == "__main__":
    # Example usage
    a = [5, 6, 7]
    b = [3, 6, 10]
    result = compare_triplets(a, b)
    print("Alice's and Bob's scores:", result)  # Output: [1, 1]
