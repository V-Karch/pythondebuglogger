# Logger

The `Logger` class is a simple logging utility for generating colored log messages with optional timestamps. It allows categorizing log messages as notices, warnings, errors, and debug information, making it easier to track the flow of execution in your applications.

## Features

- Customizable message colors using hexadecimal values or default settings.
- Supports timestamps for log messages.
- Generates ANSI escape codes for colored output in terminal environments.

## Installation

To use the `Logger` class, simply include it in your project. You can copy the class definition directly into your Python script or save it as a module.

## Usage

### Creating a Logger Instance

To create an instance of the `Logger`, you can specify custom colors or use the default ones:

```python
from pythondebuglogger.Logger import Logger

# Create a Logger instance with default colors
logger: Logger = Logger()

# Create a Logger instance with custom colors
custom_logger = Logger(notice_color=0x00FF00, warning_color=0xFFFF00, error_color=0xFF0000)
```

## Logging Messages

You can log messages for the following methods:

- **Notices**: For general information
- **Warnings**: For potential issues
- **Errors**: For critical issues
- **Debug**: For debugging information

Here's how to use the logging methods:

```python
# Log a notice
logger.display_notice("This is a notice message.")

# Log a warning
logger.display_warning("This is a warning message.")

# Log an error
logger.display_error("This is an error message.")

# Log debug information
logger.display_debug("This is a debug message.")
```

## Timestamp Option

To enable timestamps in your log messages, create the logger with the `enable_timestamps` parameter set to `True`:

```python
timestamped_logger = Logger(enable_timestamps=True)
timestamped_logger.display_notice("This is a timestamped notice message.")
```

## API Reference

### Class: `Logger`

#### Attributes

- `defaults`: A dictionary containing default color values for various log levels.
- `maximum_hex`: The maximum hexadecimal value allowed for color inputs (0xFFFFFF).

#### Methods

- `hex_to_rgb(hex: int) -> tuple[int, int, int]`: Converts a hexadecimal color value to an RGB tuple.
- `rgb_to_escape_sequence(RGB: tuple[int, int, int]) -> str`: Converts an RGB tuple to an ANSI escape code.
- `create_notice(message: str) -> str`: Creates a formatted notice message.
- `display_notice(message: str) -> None`: Displays a notice message to stdout.
- `create_warning(message: str) -> str`: Creates a formatted warning message.
- `display_warning(message: str) -> None`: Displays a warning message to stdout.
- `create_error(message: str) -> str`: Creates a formatted error message.
- `display_error(message: str) -> None`: Displays an error message to stdout.
- `create_debug(message: str) -> str`: Creates a formatted debug message.
- `display_debug(message: str) -> None`: Displays a debug message to stdout.


## Example
Here is a complete example demonstrating the usage of the Logger class:
```python
from pythondebuglogger.Logger import Logger

logger: Logger = Logger(enable_timestamps=True)

logger.display_notice("Application started.")
logger.display_warning("Low disk space warning.")
logger.display_error("Failed to load configuration.")
logger.display_debug("Debug information here.")
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

