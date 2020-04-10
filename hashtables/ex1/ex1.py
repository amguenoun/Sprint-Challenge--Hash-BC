#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = None
    duplicates = None

    for i in range(len(weights)):
        prev = hash_table_retrieve(ht, weights[i])
        if prev is not None and weights[i] * 2 == limit:
            duplicates = (i, hash_table_retrieve(ht, weights[i]))
            return duplicates
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        first = weights[i]
        if hash_table_retrieve(ht, limit - first):
            second = limit - first
            if hash_table_retrieve(ht, first) > hash_table_retrieve(ht, second):
                answer = (hash_table_retrieve(ht, first),
                          hash_table_retrieve(ht, second))
            elif first == second:
                holder = hash_table_retrieve(ht, first)
                hash_table_remove(ht, first)
                answer = (holder, hash_table_retrieve(ht, second))
            else:
                answer = (hash_table_retrieve(ht, second),
                          hash_table_retrieve(ht, first))

    if answer:
        return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
