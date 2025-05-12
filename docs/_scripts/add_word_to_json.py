import json
import os

# Path to the JSON file
json_path = "vocab_word_definitions.json"

def load_vocab(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_vocab(vocab, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(vocab, f, indent=2)

def add_words_loop(vocab):
    print("Enter new words and definitions. Type 'exit' to stop.\n")
    while True:
        word = input("Enter a new word (or 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break
        if word in vocab:
            print(f"'{word}' already exists.")
            print(f"Current definition: {vocab[word]}")
            overwrite = input("Do you want to overwrite it? (y/N): ").strip().lower()
            if overwrite != 'y':
                print("Skipping...\n")
                continue

        definition = input(f"Enter the definition for '{word}': ").strip()
        vocab[word] = definition
        print(f"'{word}' added/updated.\n")

    return dict(sorted(vocab.items()))

def main():
    vocab = load_vocab(json_path)
    updated_vocab = add_words_loop(vocab)
    save_vocab(updated_vocab, json_path)
    print(f"Vocabulary updated and saved to '{json_path}'.")

if __name__ == "__main__":
    main()
