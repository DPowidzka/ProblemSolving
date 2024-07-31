n = int(input())
arr = map(int, input().split())
scores = set(list(arr)) #remove duplicates
sorted_scores = sorted(scores)
print(sorted_scores[-2])

