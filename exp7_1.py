def read_file_to_list(file_path):
    try:
        with open(file_path,'r')as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"error:the file'{file_path}' was not found.")
        return []
file_path = "exp6_7.py"
lines_list = read_file_to_list(file_path)
if lines_list:
    print("lines from the file:")
    for line in lines_list:
        print(line)
~                      
