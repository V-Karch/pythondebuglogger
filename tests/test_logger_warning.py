from Logger import Logger


def test_logger_warning_defaults_1():
    logger: Logger = Logger()

    expected_warning_created = (
        "\033[38;2;255;236;51m[WARNING] Something Happened\033[0m"
    )
    actual_warning_created = logger.create_warning("Something Happened")

    assert expected_warning_created == actual_warning_created


def test_logger_warning_defaults_2():
    logger: Logger = Logger()

    expected_warning_created = "\033[38;2;255;236;51m[WARNING] \033[0m"
    actual_warning_created = logger.create_warning("")

    assert expected_warning_created == actual_warning_created


def test_logger_warning_defaults_3():
    logger: Logger = Logger()

    expected_warning_created = "\033[38;2;255;236;51m[WARNING] Hello World\033[0m"
    actual_warning_created = logger.create_warning("Hello World")

    assert expected_warning_created == actual_warning_created


def test_logger_warning_provided_1():
    supplied_warning_color: int = 0x00FF00

    logger: Logger = Logger(warning_color=supplied_warning_color)

    expected_warning_created = "\033[38;2;0;255;0m[WARNING] Hello World\033[0m"
    actual_warning_created = logger.create_warning("Hello World")

    assert expected_warning_created == actual_warning_created


def test_logger_warning_provided_2():
    supplied_warning_color: int = 0x00FFFF

    logger: Logger = Logger(warning_color=supplied_warning_color)

    expected_warning_created = "\033[38;2;0;255;255m[WARNING] Hello World\033[0m"
    actual_warning_created = logger.create_warning("Hello World")

    assert expected_warning_created == actual_warning_created


def test_logger_warning_provided_3():
    supplied_warning_color: int = 0xFFFFFF

    logger: Logger = Logger(warning_color=supplied_warning_color)

    expected_warning_created = "\033[38;2;255;255;255m[WARNING] Hello World\033[0m"
    actual_warning_created = logger.create_warning("Hello World")

    assert expected_warning_created == actual_warning_created
