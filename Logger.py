class Logger:
    @staticmethod
    def hex_to_rgb(hex: int) -> tuple[int, int, int]:
        """
        Given a hex input, such as 0xFF00FF
        will return the value as an RGB tuple.

        For example: 0xFF00FF -> (255, 0, 255)
        """
        red: int = (hex >> 16) & 0xFF
        green: int = (hex >> 8) & 0xFF
        blue: int = hex & 0xFF

        return (red, green, blue)

    def __init__(self, NOTICE_COLOR=None, WARNING_COLOR=None, ERROR_COLOR=None) -> None:
        ...
