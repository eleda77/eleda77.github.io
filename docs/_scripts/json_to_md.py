import json
from collections import defaultdict
import string

def json_to_markdown(json_path, md_output_path):
    # Load JSON
    with open(json_path, "r", encoding="utf-8") as f:
        vocab = json.load(f)

    # Sort and group by first letter
    grouped = defaultdict(list)
    for word, definition in sorted(vocab.items()):
        first_letter = word[0].upper()
        if first_letter in string.ascii_uppercase:
            grouped[first_letter].append((word, definition))
        else:
            grouped["#"].append((word, definition))  # For non-alpha starts

    # Header and intro
    lines = [
        "---",
        "layout: vocab",
        "title: Word Collection",
        "---",
        "## A List of Esoteric Words {#header-title-0}",
        "These are some words I have collected over the past few months, many of them coming from Terry Pratchett's *Discworld* series. I thought it might be fun to have a collection of new and unusual words together with their definitions in my own sort of personal dictionary. Please note that definitions are generally not my own, and I choose either the one I didn't know or the ones that I find most interesting/relevant.",
        "",
        "**Current Favourite Word:** snaffle",
        "",
        "**Runner-Up:** yomp (just say it, it's so fun to say)",
        "",
        "**Award for Uselessness:** moisty",
        ""
    ]

    # Add each letter section
    header_count = 1
    for letter in sorted(grouped.keys()):
        lines.append(f"### {letter} {{#header-title-{header_count}}}")
        for word, definition in grouped[letter]:
            lines.append(f"**{word}** - {definition}\n")
        lines.append("")  # spacing
        # lines.append("")
        header_count += 1

    # Save output
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# Example usage
json_to_markdown("vocab_word_definitions.json", "../vocab_list.md")
