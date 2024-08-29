from Logger import Logger


def test_logger_debug_defaults_1():
    logger: Logger = Logger()

    expected_debug_created = "\033[38;2;173;255;252m[DEBUG] Something Happened\033[0m"
    actual_debug_created = logger.create_debug("Something Happened")

    assert expected_debug_created == actual_debug_created


def test_logger_debug_defaults_2():
    logger: Logger = Logger()

    expected_debug_created = "\033[38;2;173;255;252m[DEBUG] \033[0m"
    actual_debug_created = logger.create_debug("")

    assert expected_debug_created == actual_debug_created


def test_logger_debug_defaults_3():
    logger: Logger = Logger()

    expected_debug_created = "\033[38;2;173;255;252m[DEBUG] Hello World\033[0m"
    actual_debug_created = logger.create_debug("Hello World")

    assert expected_debug_created == actual_debug_created


def test_logger_debug_provided_1():
    supplied_debug_color: int = 0x00FF00

    logger: Logger = Logger(debug_color=supplied_debug_color)

    expected_debug_created = "\033[38;2;0;255;0m[DEBUG] Hello World\033[0m"
    actual_debug_created = logger.create_debug("Hello World")

    assert expected_debug_created == actual_debug_created


def test_logger_debug_provided_2():
    supplied_debug_color: int = 0x00FFFF

    logger: Logger = Logger(debug_color=supplied_debug_color)

    expected_debug_created = "\033[38;2;0;255;255m[DEBUG] Hello World\033[0m"
    actual_debug_created = logger.create_debug("Hello World")

    assert expected_debug_created == actual_debug_created


def test_logger_debug_provided_3():
    supplied_debug_color: int = 0xFFFFFF

    logger: Logger = Logger(debug_color=supplied_debug_color)

    expected_debug_created = "\033[38;2;255;255;255m[DEBUG] Hello World\033[0m"
    actual_debug_created = logger.create_debug("Hello World")

    assert expected_debug_created == actual_debug_created
