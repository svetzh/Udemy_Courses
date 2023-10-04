"""
Linked List is like list but without INDEXES
Node is both value and pointer like dictionary

Nodes are spread all over the memory
head -> is variable that points to the first node of the LL
tail -> is variable that points to the last node of the LL
pointer -> is pointing to the next, next..., until is None
"""


head = {
    "стойност": 11,
    "следващ": {
        "стойност": 3,
        "следващ": {
            "стойност": 23,
            "следващ": {
                "стойност": 7,
                "следващ": None
            }
        }
    }
}


print(head["следващ"]["следващ"]["стойност"])
print()
