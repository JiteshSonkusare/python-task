from typing import List

def gen_params(a: str, b: str) -> List[str]:
    """
    Find the set of common elements in the two inputs (case-insensitive).
    Return them as a unique list of lower case strings.
    Do not include partial matches (e.g. "pineapple" and "apple").
    """
    a_lower = set(a.lower().split(","))
    b_lower = set(b.lower().split())
    common_elements = a_lower.intersection(b_lower)
    return list(common_elements)


a_input = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
b_input = "Frog  apple    fox cat fish fish"
result = gen_params(a_input, b_input)
print(result)