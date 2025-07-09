#!/usr/bin/env python3
"""
Apathy Theme Demo - Python
Showcases Python syntax highlighting features
"""

import asyncio
import json
import re
from typing import List, Dict, Optional, Union, Any
from dataclasses import dataclass
from enum import Enum


class ThemeType(Enum):
    """Theme type enumeration"""

    DARK = "dark"
    LIGHT = "light"
    HIGH_CONTRAST = "high_contrast"


@dataclass
class ColorScheme:
    """Color scheme data class"""

    name: str
    background: str
    foreground: str
    accent: str
    is_default: bool = False


class ApathyTheme:
    """
    Main theme class demonstrating various Python features
    TODO: Add more color schemes
    FIXME: Optimize color calculations
    """

    def __init__(self, name: str = "Apathy"):
        self.name = name
        self.version = "1.0.0"
        self._colors: Dict[str, str] = {
            "background": "#0F0D1A",
            "foreground": "#E6E2D1",
            "accent": "#FF7A00",
        }
        self._is_active = True

    def process_data(self, data: List[Union[str, int]]) -> List[str]:
        """Process data with list comprehension and type hints"""
        # List comprehension with conditional
        processed = [str(item).upper() for item in data if item is not None]

        # Generator expression
        lengths = (len(item) for item in processed)

        # Dictionary comprehension
        result_dict = {item: len(item) for item in processed}

        return processed

    @property
    def colors(self) -> Dict[str, str]:
        """Get theme colors"""
        return self._colors.copy()

    @colors.setter
    def colors(self, value: Dict[str, str]) -> None:
        """Set theme colors"""
        if not isinstance(value, dict):
            raise TypeError("Colors must be a dictionary")
        self._colors.update(value)

    def get_color(self, name: str, default: str = "#FFFFFF") -> str:
        """Get a specific color by name"""
        return self._colors.get(name, default)

    def set_color(self, name: str, value: str) -> None:
        """Set a specific color"""
        if not re.match(r"^#[0-9A-Fa-f]{6}$", value):
            raise ValueError(f"Invalid color format: {value}")
        self._colors[name] = value

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def __str__(self) -> str:
        """String representation"""
        return f"ApathyTheme(name='{self.name}', version='{self.version}')"

    def __repr__(self) -> str:
        """Developer representation"""
        return f"ApathyTheme(name='{self.name}', colors={len(self._colors)} colors)"

    def __enter__(self):
        """Context manager entry"""
        print(f"Activating theme: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        print(f"Deactivating theme: {self.name}")
        self._is_active = False


# Global variables and constants
THEME_CONFIG = {
    "default_theme": "Apathy",
    "supported_formats": ["json", "yaml", "toml"],
    "max_colors": 256,
}


# Function with decorators
def theme_validator(func):
    """Decorator for theme validation"""

    def wrapper(*args, **kwargs):
        print(f"Validating theme operation: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Theme operation completed: {func.__name__}")
        return result

    return wrapper


@theme_validator
def create_color_scheme(name: str, colors: Dict[str, str]) -> ColorScheme:
    """Create a new color scheme"""
    return ColorScheme(
        name=name,
        background=colors.get("background", "#000000"),
        foreground=colors.get("foreground", "#FFFFFF"),
        accent=colors.get("accent", "#FF0000"),
    )


# Lambda functions
gradient_calculator = lambda start, end, steps: [
    f"#{int(start + (end - start) * i / steps):06x}" for i in range(steps + 1)
]


# Exception handling
def safe_color_conversion(color_value: str) -> Optional[tuple]:
    """Safely convert color with exception handling"""
    try:
        if color_value.startswith("#"):
            return ApathyTheme.hex_to_rgb(color_value)
        elif color_value.startswith("rgb"):
            # Extract RGB values with regex
            match = re.search(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", color_value)
            if match:
                return tuple(map(int, match.groups()))
        else:
            raise ValueError("Unsupported color format")
    except (ValueError, AttributeError) as e:
        print(f"Color conversion error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        print("Color conversion attempt completed")


# Main execution
if __name__ == "__main__":
    # Create theme instance
    theme = ApathyTheme("Apathy VS Code")

    # Demonstrate various features
    print(f"Theme: {theme}")
    print(f"Colors: {theme.colors}")

    # Context manager usage
    with theme as active_theme:
        # String formatting
        message = f"""
        Theme Information:
        Name: {active_theme.name}
        Version: {active_theme.version}
        Background: {active_theme.get_color('background')}
        """
        print(message)

    # F-string with expressions
    color_count = len(theme.colors)
    summary = f"Theme '{theme.name}' has {color_count} color{'s' if color_count != 1 else ''} defined"
    print(summary)

    # Async execution
    async def main():
        result = await theme.async_operation()
        print(result)

    # Run async function
    asyncio.run(main())
