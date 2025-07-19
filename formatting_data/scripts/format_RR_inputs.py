import sys

statements = []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} input_file_name output_file_name.csv")
        sys.exit()

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    with open(input_file_name, "r") as file:
        for line in file:
            statements.append(line.split("\t"))
    with open(output_file_name, "w") as file:
        file.write(f"station name, parameter\n")
        for statement in statements:
            file.write(f"{statement[0]}, {statement[1]}")
