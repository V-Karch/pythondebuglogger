class Logger:

    defaults: dict[str, str] = {
        "default_notice_color": "\033[38;2;r;g;bm",
        "default_warning_color": "\033[38;2;r;g;bm",
        "default_error_color": "\033[38;2;r;g;bm",
        "reset_color": "\033[0m"
    } # Dictionary of default values for logging

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
        ...
