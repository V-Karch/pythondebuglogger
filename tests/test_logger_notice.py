from Logger import Logger


def test_logger_notice_defaults_1():
    logger: Logger = Logger()

    expected_notice_created = "\033[38;2;129;255;126m[NOTICE] Something Happened\033[0m"
    actual_notice_created = logger.create_notice("Something Happened")

    assert expected_notice_created == actual_notice_created


def test_logger_notice_defaults_2():
    logger: Logger = Logger()

    expected_notice_created = "\033[38;2;129;255;126m[NOTICE] \033[0m"
    actual_notice_created = logger.create_notice("")

    assert expected_notice_created == actual_notice_created


def test_logger_notice_defaults_3():
    logger: Logger = Logger()

    expected_notice_created = "\033[38;2;129;255;126m[NOTICE] Hello World\033[0m"
    actual_notice_created = logger.create_notice("Hello World")

    assert expected_notice_created == actual_notice_created


def test_logger_notice_provided_1():
    supplied_notice_color: int = 0x00FF00

    logger: Logger = Logger(notice_color=supplied_notice_color)

    expected_notice_created = "\033[38;2;0;255;0m[NOTICE] Hello World\033[0m"
    actual_notice_created = logger.create_notice("Hello World")

    assert expected_notice_created == actual_notice_created


def test_logger_notice_provided_2():
    supplied_notice_color: int = 0x00FFFF

    logger: Logger = Logger(notice_color=supplied_notice_color)

    expected_notice_created = "\033[38;2;0;255;255m[NOTICE] Hello World\033[0m"
    actual_notice_created = logger.create_notice("Hello World")

    assert expected_notice_created == actual_notice_created


def test_logger_notice_provided_2():
    supplied_notice_color: int = 0xFFFFFF

    logger: Logger = Logger(notice_color=supplied_notice_color)

    expected_notice_created = "\033[38;2;255;255;255m[NOTICE] Hello World\033[0m"
    actual_notice_created = logger.create_notice("Hello World")

    assert expected_notice_created == actual_notice_created
