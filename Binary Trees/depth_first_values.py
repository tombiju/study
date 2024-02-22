class Node:
  def __init__(self, value=None, right=None, left=None):
    self.right = right
    self.left = left
    self.value = value

def depth_first_values(stack: list, visited: list) -> list:
    if stack:
        current = stack.pop()
        visited.append(current.value)
        if (current.right):
            stack.append(current.right)
        if (current.left):
            stack.append(current.left)
        depth_first_values(stack, visited)
    return visited
    

if __name__ == "__main__":
    a = Node('a');
    b = Node('b');
    c = Node('c');
    d = Node('d');
    e = Node('e');
    f = Node('f');

    a.left = b;
    a.right = c;
    b.left = d;
    b.right = e;
    c.right = f;

    # //      a
    # //    /   \
    # //   b     c
    # //  / \     \
    # // d   e     f

    assert depth_first_values([a], []) == ['a', 'b', 'd', 'e', 'c', 'f']

    a = Node('a');
    b = Node('b');
    c = Node('c');
    d = Node('d');
    e = Node('e');
    f = Node('f');
    g = Node('g');

    a.left = b;
    a.right = c;
    b.left = d;
    b.right = e;
    c.right = f;
    e.left = g;

    # //      a
    # //    /   \
    # //   b     c
    # //  / \     \
    # // d   e     f
    # //    /
    # //   g

    assert depth_first_values([a], []) == ['a', 'b', 'd', 'e', 'g', 'c', 'f']

    a = Node('a');
    # //      a
    assert depth_first_values([a], []) == ['a']

    a = Node('a');
    b = Node('b');
    c = Node('c');
    d = Node('d');
    e = Node('e');

    a.right = b;
    b.left = c;
    c.right = d;
    d.right = e;

    # //      a
    # //       \
    # //        b
    # //       /
    # //      c
    # //       \
    # //        d
    # //         \
    # //          e

    depth_first_values(None, []) == []