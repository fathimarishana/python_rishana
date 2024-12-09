input_file = input("enter the input file peth:")
output_file = input("enter the output file peth:")
try:
    with open(input_file,'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile, start=1):
            if i % 2 != 0:
                 outfile.write(line)
    print(f"odd lines from {input_file} have been copied to {output_file}")
except FileNotFoundError:
    print(f"the file {input_file} was not found.")
except Exception as e:
    print(f"an error occurred:{e}")
~                                     
~                                     
