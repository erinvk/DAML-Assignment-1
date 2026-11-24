import os

os.makedirs("data_cleaned", exist_ok=True)

for filename in sorted(os.listdir("data")):
    if not filename.endswith(".txt"):
        continue
    in_path = os.path.join("data", filename)
    with open(in_path, encoding="utf-8") as f:
        text = f.read()
    start = text.find("*** START OF")
    if start == -1:
        raise ValueError(f"no Project Gutenberg start marker in {in_path}")
    start = text.find("\n", start) + 1
    end = text.find("*** END OF", start)
    if end == -1:
        raise ValueError(f"no Project Gutenberg end marker in {in_path}")
    out_path = os.path.join("data_cleaned", filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text[start:end].strip() + "\n")
