
'''
rough building blocks

Built a list of nodes, to process:

But had an interesting problem when creating a simple pull from the file
1. had to remove the "\n" after nodes
2. remove duplicates
3. remove blank lines
'''


infile = "node_list.txt"

def read_file(file_name):

    # returns a dictionary of node names
    # no value att
    node_name = {}

    with open(file_name) as file:
        for node in file:
            clean_node = node.strip()
            if len(clean_node) > 1:
                node_name[clean_node] = 1

    return node_name



# simple setup
node_list = read_file(infile)
incr = 1
for node in node_list:
    print(str(incr) + " : " + node)
    incr += 1

