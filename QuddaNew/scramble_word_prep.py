from collections import defaultdict

with open(
    "data\\scramble_words.txt", "wt"
) as out, open(
    "data\\scramble_words_original.txt"
) as src:
    final = []
    stats = defaultdict(int)

    for word in src.read().split("\n"):
        unique_chars = set()

        for char in word:
            unique_chars.add(char)

        if (
            len(word) > 3 and 
            len(unique_chars) > 4  and 
            len(unique_chars) < len(word) 
            and len(word) < 7
        ):
            print(f"Added word {word}")

            stats[word[0]] += 1

            final.append(word)

    i = out.write('\n'.join(final))
    print(f"Wrote {len(final)} words in {i} bytes")
    print("Stats")
    print('\n'.join([f"{k}: {stats[k]}" for k in stats]))