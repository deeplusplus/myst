from anytree import Node, RenderTree


def build_tree(node, iteration):
    if iteration == 15:
        return
    iteration += 1
    left_branch = Node(pull_left_lever(node.name))
    right_branch = Node(pull_right_lever(node.name))

    left_branch.parent = node
    right_branch.parent = node

    build_tree(left_branch, iteration)
    build_tree(right_branch, iteration)

# given single digit, returns digit advanced by 1
def advance_number(number):
    if number == "3":
        return "2"
    elif number == "2":
        return "1"
    elif number == "1":
        return "3"

# takes list of str and increments index 1 and 2
def pull_left_lever(number_str):
    number_list = [digit for digit in number_str]
    return number_list[0] + advance_number(number_list[1]) +  advance_number(number_list[2])


# takes list of str and incremember index 0 and 1
def pull_right_lever(number_str):
    number_list = [digit for digit in number_str]
    return advance_number(number_list[0]) + advance_number(number_list[1]) + number_list[2]

parent_node = Node("221")

build_tree(parent_node, 1)

foo = str(RenderTree(parent_node).by_attr("name"))

f = open("output.txt", "w", encoding="utf-8")
f.write(foo)
f.close()
