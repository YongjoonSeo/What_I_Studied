from collections import deque
import itertools

def MergeSort(deck):
    mid = (0 + len(deck)) // 2
    if len(deck) == 1:
        return deck
    elif len(deck) == 2:
        if deck[0] > deck[1]:
            deck.append(deck.popleft())
        return deck
    else:
        resultdeck = deque()
        deck1 = MergeSort(deque(itertools.islice(deck, 0, mid)))
        deck2 = MergeSort(deque(itertools.islice(deck, mid, len(deck))))
        i, j = -len(deck1), -len(deck2)
        while i < 0 or j < 0:
            if i == 0:
                resultdeck.append(deck2[j])
                j += 1
            elif j == 0:
                resultdeck.append(deck1[i])
                i += 1
            else:
                if deck1[i] < deck2[j]:
                    resultdeck.append(deck1[i])
                    i += 1
                else:
                    resultdeck.append(deck2[j])
                    j += 1
        return resultdeck

sample = deque([69, 10, 30, 2, 16, 8, 31, 22])
print(MergeSort(sample))