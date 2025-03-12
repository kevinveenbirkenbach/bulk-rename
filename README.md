# Bulk Rename 🚀
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


Bulk Rename is a Python-based command-line tool that renames files in bulk by replacing specified substrings in their filenames. It supports both recursive and non-recursive renaming, and it’s installable via [Kevin's Package-Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `bure`.

## Features ✨

- **Bulk File Renaming:** Replace a specified substring in file names with a new string.
- **Recursive Option:** Rename files in subdirectories using the `-r` or `--recursive` flag.
- **Verbose Output:** Displays each renaming action for clear tracking.

## Installation 📦

Install Bulk Rename via [Kevin's Package-Manager](https://github.com/kevinveenbirkenbach/package-manager):

```bash
pkgmgr clone bulk-rename
pkgmgr install bulk-rename
```

Once installed, you can call the tool globally with the alias:

```bash
bure search_string replacement_string [options]
```

## Usage 🛠️

The main script is stored in `main.py`. You can run it directly:

```bash
./main.py search_string replacement_string [-r|--recursive]
```

- **search_string:** The substring to search for in file names.
- **replacement_string:** The substring to replace the search string with.
- **-r, --recursive:** (Optional) Recursively rename files in all subdirectories.

## License 📝

This project is licensed under the [MIT License](LICENSE).

## Author

**Kevin Veen-Birkenbach**  
Visit my website: [https://www.veen.world/](https://www.veen.world/)

## Credits 🤖

This tool was created with the help of [ChatGPT](https://chat.openai.com). Check out [this conversation]([https://chat.openai.com/chat](https://chatgpt.com/share/67d1328b-5384-800f-a2ec-7ddd5b5e861d)) for more details!
