from graphs_trees.graphs_dependencies.graphs_dependencies import Dependency, BuildOrder


def test_graphs_dependencies():
    dependencies = [
        Dependency('d', 'g'),
        Dependency('f', 'c'),
        Dependency('f', 'b'),
        Dependency('f', 'a'),
        Dependency('c', 'a'),
        Dependency('b', 'a'),
        Dependency('a', 'e'),
        Dependency('b', 'e'),
    ]

    build_order = BuildOrder(dependencies, "Build Order")
    processed_nodes = build_order.find_build_order()

    expected_result0 = ('d', 'f')
    expected_result1 = ('c', 'b', 'g')
    assert processed_nodes[0] in expected_result0
    assert processed_nodes[1] in expected_result0
    assert processed_nodes[2] in expected_result1
    assert processed_nodes[3] in expected_result1
    assert processed_nodes[4] in expected_result1
    assert processed_nodes[5] is 'a'
    assert processed_nodes[6] is 'e'
