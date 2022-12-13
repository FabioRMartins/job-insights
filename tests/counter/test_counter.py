from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word_python = "Python"
    word_javascript = "Javascript"

    counter_python = count_ocurrences(path, word_python)

    assert counter_python == 1639

    counter_javascript = count_ocurrences(path, word_javascript)

    assert counter_javascript == 122
