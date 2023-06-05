
# Track Frequency
import collections
def Track_Frequency(List):
    return dict(collections.Counter(List))
print(Track_Frequency([10, 10, 12, 12, 10, 13, 13, 14]))
# Output
# {10: 3, 12: 2, 13: 2, 14: 1}