import os

LINE = "I am away on a year-long vacation in direct sunlight. No one has asked me anything. I do not miss working."


assert 1 <= len(LINE) <= 120, "LINE must be between 1 and 120 characters"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(output_path, "r", encoding="utf-8", newline="") as f:
        data = f.read()

    char_count = len(data)
    if not (1 <= char_count <= 120):
        raise RuntimeError("written file must be 1 to 120 characters, got %d" % char_count)

    print(output_path)
    print(char_count)


if __name__ == "__main__":
    main()
