def parse_version(version):
    major, minor, fix = version.split('.')
    return int(major), int(minor), fix


def test_tensorflow():
    import tensorflow
    major, _, _ = parse_version(tensorflow.__version__)
    assert major >= 1


def test_keras():
    import keras
    major, _, _ = parse_version(keras.__version__)
    assert major >= 2