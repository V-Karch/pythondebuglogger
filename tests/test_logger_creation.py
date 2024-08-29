from Logger import Logger


def test_logger_creation_no_args():
    logger: Logger = Logger()

    expected_default_notice_color = "\033[38;2;129;255;126m"
    expected_default_warning_color = "\033[38;2;255;236;51m"
    expected_default_error_color = "\033[38;2;255;91;91m"

    actual_default_notice_color = logger.notice_color
    actual_default_warning_color = logger.warning_color
    actual_default_error_color = logger.error_color

    assert expected_default_notice_color == actual_default_notice_color
    assert expected_default_warning_color == actual_default_warning_color
    assert expected_default_error_color == actual_default_error_color


def test_logger_creation_with_args():
    supplied_notice_color: int = 0x00FF00
    supplied_warning_color: int = 0xFFFF00
    supplied_error_color: int = 0xFF0000

    logger: Logger = Logger(
        notice_color=supplied_notice_color,
        warning_color=supplied_warning_color,
        error_color=supplied_error_color,
    )

    expected_notice_color: str = "\033[38;2;0;255;0m"
    expected_warning_color: str = "\033[38;2;255;255;0m"
    expected_error_color: str = "\033[38;2;255;0;0m"

    actual_notice_color: str = logger.notice_color
    actual_warning_color: str = logger.warning_color
    actual_error_color: str = logger.error_color

    assert expected_notice_color == actual_notice_color
    assert expected_warning_color == actual_warning_color
    assert expected_error_color == actual_error_color