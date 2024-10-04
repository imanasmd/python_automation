# Python Regular Expressions: A Comprehensive Guide

Welcome to the **Python Automation** GitHub repository, where you'll find code examples and detailed explanations on mastering **regular expressions (regex)** in Python. This repository provides insights and examples covering various regex concepts, helping you handle text data efficiently.

---

## Table of Contents

1. [Introduction to Regular Expressions in Python](#introduction)
2. [Shorthand Character Classes](#shorthand-character-classes)
3. [Matching Specific Patterns](#matching-specific-patterns)
4. [Handling Hyphens in Mobile Numbers](#handling-hyphens-in-mobile-numbers)
5. [Working with IP Addresses](#working-with-ip-addresses)
6. [Using Special Characters](#using-special-characters)
7. [Advanced Regex Patterns](#advanced-regex-patterns)
    - [Pipe (`|`) for Multiple Matches](#pipe-for-multiple-matches)
    - [Question Mark (`?`) for Optional Matching](#question-mark-for-optional-matching)
    - [Asterisk (`*`) for Zero or More Occurrences](#asterisk-for-zero-or-more-occurrences)
    - [Plus (`+`) for One or More Occurrences](#plus-for-one-or-more-occurrences)
    - [Anchors (`^` and `$`)](#anchors)
    - [Wildcard (`.`)](#wildcard)

---

## Introduction

In the world of programming, efficiently working with text data is crucial. **Regular expressions (regex)** offer powerful solutions for searching, extracting, and manipulating patterns in text. In Python, the `re` module simplifies regex operations. This repository will guide you through regex basics, key concepts, and practical examples for solving real-world problems.

Explore the repository to find code samples and best practices in text processing using Python regex. 

---

## Shorthand Character Classes

Shorthand character classes are used to match specific types of characters, reducing the need for complex patterns. Here are some commonly used shorthand classes:

- **`\d`** – Matches any digit (equivalent to `[0-9]`).
- **`\D`** – Matches any non-digit (equivalent to `[^0-9]`).
- **`\w`** – Matches any alphanumeric character or underscore (equivalent to `[a-zA-Z0-9_]`).
- **`\W`** – Matches any non-alphanumeric character (equivalent to `[^a-zA-Z0-9_]`).
- **`\s`** – Matches any whitespace character.
- **`\S`** – Matches any non-whitespace character.

Refer to the file [first.py](Day-2/first.py) for examples on using these character classes.

---

## Matching Specific Patterns

Instead of using the `compile()` function, you can directly pass a regex pattern as a raw string to the `search()` method. For example, extracting a mobile number from user input without explicitly compiling the regex is more efficient. Explore the example in [second.py](Day-2/second.py).

---

## Handling Hyphens in Mobile Numbers

Mobile numbers may contain hyphens, but you can extract specific sequences like three or four digits using regex. Check out [third.py](Day-2/third.py) to learn how to ignore hyphens and focus on the digit patterns.

---

## Working with IP Addresses

Matching IP addresses, which contain groups of two or three digits, can be challenging. Curly braces `{min, max}` allow you to define the minimum and maximum occurrences for each segment of the IP address. See the detailed example in [fourth.py](Day-2/fourth.py).

---

## Using Special Characters

When searching for special characters like `!@#$%^&*(){}[]/~\`, you need to escape them with a backslash (`\`). For example, to match `@`, `#`, or `$`, use `\@`, `\#`, or `\$`. Learn more in [fifth.py](Day-2/fifth.py).

---

## Advanced Regex Patterns

### Pipe (`|`) for Multiple Matches

The pipe (`|`) character allows you to match one of several patterns. For instance, `Carrot|Parrot` will match either "Carrot" or "Parrot". The first match is returned as a Match object. See examples in [sixth.py](Day-2/sixth.py).

### Question Mark (`?`) for Optional Matching

Use the question mark (`?`) to mark parts of a pattern as optional. It tells the regex to match whether that part is present or not. Explore the code in [seventh.py](Day-2/seventh.py).

### Asterisk (`*`) for Zero or More Occurrences

The asterisk (`*`) is used to match zero or more occurrences of the preceding character or group. Check [eighth.py](Day-2/eighth.py) for examples.

### Plus (`+`) for One or More Occurrences

The plus (`+`) ensures that the pattern preceding it appears at least once. It’s useful for matching repeating sequences. See [ninth.py](Day-2/ninth.py) for detailed examples.

### Anchors (`^` and `$`)

Anchors like `^` (caret) and `$` (dollar sign) ensure that your pattern is matched either at the start or the end of the string, respectively. Learn more in [tenth.py](Day-2/tenth.py).

### Wildcard (`.`)

The dot (`.`) character is a wildcard that matches any character except for a newline. It is commonly used to create flexible patterns. Check out examples in [eleventh.py](Day-2/eleventh.py).

---

## Contributing

Feel free to explore the repository, submit pull requests, or raise issues if you find any bugs or improvements. Your contributions are welcome!

---




**Explore more in the [GitHub repository](https://github.com/imanasmd/python_automation.git).**
