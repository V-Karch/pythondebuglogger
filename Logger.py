class Logger:
    defaults: dict[str, str] = {
        "default_notice_color": "\033[38;2;129;255;126m",
        "default_warning_color": "\033[38;2;255;236;51m",
        "default_error_color": "\033[38;2;255;91;91m",
        "reset_color": "\033[0m",
    }  # Dictionary of default values for logging

    maximum_hex: int = 16777215

    @staticmethod
    def hex_to_rgb(hex: int) -> tuple[int, int, int]:
        """
        Given a hex input, such as 0xFF00FF
        will return the value as an RGB tuple.

        For example: 0xFF00FF -> (255, 0, 255)
        """

        if hex > Logger.maximum_hex:
            raise ValueError("Hex value must be less than or equal to 0xFFFFFF")

        red: int = (hex >> 16) & 0xFF
        green: int = (hex >> 8) & 0xFF
        blue: int = hex & 0xFF

        return (red, green, blue)

    @staticmethod
    def rgb_to_escape_sequence(RGB: tuple[int, int, int]) -> str:
        return f"\033[38;2;{RGB[0]};{RGB[1]};{RGB[2]}m"

    def __init__(self, notice_color=None, warning_color=None, error_color=None) -> None:
        """
        Accepts a hex input for each optional color
        if no color is provided, the defaults will be assumed

        Example logger creation:

        logger: Logger = Logger(notice_color=0x00FF00, warning_color=0xFFFF00, error_color=0x0000FF)
        """

        self.reset_color = Logger.defaults.get("reset_color")

        # Assigning instance variables
        if notice_color is None:
            self.notice_color: str = Logger.defaults.get("default_notice_color")
        else:
            self.notice_color: str = Logger.rgb_to_escape_sequence(
                Logger.hex_to_rgb(notice_color)
            )

        if warning_color is None:
            self.warning_color: str = Logger.defaults.get("default_warning_color")
        else:
            self.warning_color: str = Logger.rgb_to_escape_sequence(
                Logger.hex_to_rgb(warning_color)
            )

        if error_color is None:
            self.error_color: str = Logger.defaults.get("default_error_color")
        else:
            self.error_color: str = Logger.rgb_to_escape_sequence(
                Logger.hex_to_rgb(error_color)
            )

    def create_notice(self, message: str) -> str:
        """Creates a notice message and returns it as a string

        Args:
            message (str): The notice message

        Returns:
            str: A string that can be sent to any stdout as a notice
        """

        return f"{self.notice_color}[NOTICE] {message}{self.reset_color}"

    def display_notice(self, message: str) -> None:
        """Displays a notice, calling Logger().create_notice() on the supplied message

        Args:
            message (str): The notice message
        """

        print(self.create_notice(message))

    def create_warning(self, message: str) -> str:
        """Creates a warning message and returns it as a string

        Args:
            message (str): The warning message

        Returns:
            str: A string that can be sent to any stdout as a warning
        """

        return f"{self.warning_color}[WARNING] {message}{self.reset_color}"

    def display_warning(self, message: str) -> None:
        """Displays a warning, calling Logger().create_warning() on the supplied message

        Args:
            message (str): The warning message
        """

        print(self.create_warning(message))

    def create_error(self, message: str) -> str:
        """Creates an error message and returns it as a string

        Args:
            message (str): The error message

        Returns:
            str: A string that can be sent to any stdout as an error
        """

        return f"{self.error_color}[ERROR] {message}{self.reset_color}"

    def display_error(self, message: str) -> None:
        """Displays an error, calling Logger.create_error() on the supplied message

        Args:
            message (str): The error message
        """

        print(self.create_error(message))
