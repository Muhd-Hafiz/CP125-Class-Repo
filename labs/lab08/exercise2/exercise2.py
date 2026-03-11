from tkinter.font import names


def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    file1 = open("labs/lab08/exercise2/data/list1.txt", "r")
    file2 = open("labs/lab08/exercise2/data/list2.txt", "r")
    
    names = set()
    
    for line in file1:
        names.add(line.strip())
    for line in file2:
        names.add(line.strip())
    
    sorted_names = sorted(names)
    file1.close()
    file2.close()
    
    f = open("labs/lab08/exercise2/data/merged.txt", "w")
    f.write("\n".join(sorted_names))
    f.close()

    return len(names)


result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
