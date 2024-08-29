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

    expected_notice_color: str = "\033[38;2;0;255;0m"
    expected_warning_color: str = "\033[38;2;255;255;0m"
    expected_error_color: str = "\033[38;2;255;0;0m"

    actual_notice_color: str = logger.notice_color
    actual_warning_color: str = logger.warning_color
    actual_error_color: str = logger.error_color

    assert expected_notice_color == actual_notice_color
    assert expected_warning_color == actual_warning_color
    assert expected_error_color == actual_error_color
