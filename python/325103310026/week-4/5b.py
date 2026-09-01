from collections import Counter

string = "aaaaabbbcccccdd"
result2 = Counter(string).most_common(2)
result3 = Counter(string).most_common(3)
print("the top 2 most frequent characters:",result2)
print("the top 3 most frequent characters:",result3)
