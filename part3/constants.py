BANNER = """PandA IR — Part 3 (Multi-word AND search)
Type :help for commands. Type :quit to exit."""

HELP = """Commands:
  :help            Show this help text
  :quit            Exit the program
  :highlight on|off
                   Toggle highlighting of matches

Usage:
  Enter one or more words to search (AND). Examples:
    love
    summer day

Notes:
  - Case-insensitive search
  - Works over the TITLE and LINES of three sonnets (shows only sonnets that contain *all* the words)
  - Print only matching sonnets
  - Show: "N out of 3 sonnets contain "<word>"."
  - Use ANSI escape codes for highlighting when enabled
  - Manual substring scan (no str.find, no 'in' for text search, no regex)
"""
