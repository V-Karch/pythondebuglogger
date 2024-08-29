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
