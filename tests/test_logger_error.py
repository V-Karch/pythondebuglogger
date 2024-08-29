from Logger import Logger


def test_logger_error_defaults_1():
    logger: Logger = Logger()

    expected_error_created = "\033[38;2;255;91;91m[ERROR] Something Happened\033[0m"
    actual_error_created = logger.create_error("Something Happened")

    assert expected_error_created == actual_error_created


def test_logger_error_defaults_2():
    logger: Logger = Logger()

    expected_error_created = "\033[38;2;255;91;91m[ERROR] \033[0m"
    actual_error_created = logger.create_error("")

    assert expected_error_created == actual_error_created


def test_logger_error_defaults_3():
    logger: Logger = Logger()

    expected_error_created = "\033[38;2;255;91;91m[ERROR] Hello World\033[0m"
    actual_error_created = logger.create_error("Hello World")

    assert expected_error_created == actual_error_created


def test_logger_error_provided_1():
    supplied_error_color: int = 0x00FF00

    logger: Logger = Logger(error_color=supplied_error_color)

    expected_error_created = "\033[38;2;0;255;0m[ERROR] Hello World\033[0m"
    actual_error_created = logger.create_error("Hello World")

    assert expected_error_created == actual_error_created


def test_logger_error_provided_2():
    supplied_error_color: int = 0x00FFFF

    logger: Logger = Logger(error_color=supplied_error_color)

    expected_error_created = "\033[38;2;0;255;255m[ERROR] Hello World\033[0m"
    actual_error_created = logger.create_error("Hello World")

    assert expected_error_created == actual_error_created


def test_logger_error_provided_3():
    supplied_error_color: int = 0xFFFFFF

    logger: Logger = Logger(error_color=supplied_error_color)

    expected_error_created = "\033[38;2;255;255;255m[ERROR] Hello World\033[0m"
    actual_error_created = logger.create_error("Hello World")

    assert expected_error_created == actual_error_created
