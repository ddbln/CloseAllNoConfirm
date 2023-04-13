# Close All without Confirmation

Effortlessly close all (unsaved and saved) files in Sublime Text without being interrupted by confirmation dialogs! This plugin is ideal for those who want to swiftly close multiple unsaved files without needing to confirm each one individually. Optionally, you can enable a single confirmation prompt before closing all files.

## Features

- Close all files without confirmation dialogs.
- Accessible via Command Palette.
- Easy-to-activate key bindings (instructions provided).
- For cautious users: Close all files with just one confirmation (optional).

## Installation

### Via Package Control

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
2. Open the command palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
3. Type `Package Control: Install Package` and press Enter.
4. Search for `Close All without Confirmation` and select it from the list to install.

### Manual Installation

1. Download or clone this repository: `https://github.com/ddbln/Close All without Confirmation`
2. Open Sublime Text and click on `Preferences > Browse Packages...` or `Settings > Browse Packages...` to open the packages directory.
3. Copy the entire `Close All without Confirmation` folder into the packages directory.

## Usage

### Command Palette

You can trigger the `Close All without Confirmation` command using the Command Palette. Press `Shift+Command+P` (Mac) or `Shift+Ctrl+P` (Windows/Linux) to open the Command Palette, then type "Close All without Confirmation" (Sublime Text autocompletes) and press Enter.

### Key Bindings

By default, ”Close All without Confirmation“ does not add key bindings. However, you can easily set up custom key bindings by following these steps:

1. Navigate to `Settings` > `Package Settings` > `Close All without Confirmation` > `Key Bindings`.
2. This will open the key bindings file in a new window. Add a new key binding entry, referring to the suggested key bindings below.

**Suggested Key Bindings**

For Windows and Linux platforms, you could use the following suggested key binding:

```json
[
    {
        "keys": ["ctrl+alt+shift+w"],
        "command": "close_all_without_confirm"
    }
]
```
for macOS:

```json
[
    {
        "keys": ["super+alt+shift+w"],
        "command": "close_all_without_confirm"
    }
]
```

## Customization

### Optional Confirmation Prompt

By default, this plugin will close all unsaved windows without any confirmation. However, if you want to enable a single confirmation prompt before closing all unsaved windows, you can add the following entry to your User settings:

```json
{
    "ask_before_closing": true
}
```

To access the settings file, in Sublime Text, simply go to `Settings` or `Preferences` and then choose > `Package Settings` > `Close All without Confirmation` > `Settings`.

## Frequently Asked Questions

**Q: Does the plugin only close unsaved files or all files?**

A: The “Close All without Confirmation“ plugin closes all files, unsaved as well as saved ones. The main benefit is that it allows you to close all files without prompting for confirmation when closing unsaved files. Dealing with multiple confirmation dialogs can quickly become a painful experience. But don’t worry, this plugin has got you covered – it closes all files swiftly and efficiently!

**Q: Why would I need this? Can you provide an example of when this plugin would be useful?**

A: Suppose you've searched and replaced a dozen or hundreds of files with a single click: saving them all is easy with Sublime Text and takes just one command (and no questions asked). But: have you ever tried to close them without saving?

**Q: Is there any risk of losing my work when using this plugin?**

A: The plugin is designed for speed and convenience, but of course accidents can happen. If you’re concerned about losing unsaved work, you can enable the optional single confirmation prompt by setting the "ask_before_closing" option to true in the [settings](#optional-confirmation-prompt). This way, you’ll get one friendly reminder to save your work before the plugin closes all files.

**Q: Will this plugin slow down my Sublime Text or cause any performance issues?**

A: No, the Close All without Confirmation plugin is lightweight and efficient. It should not cause any noticeable performance issues in your Sublime Text environment.

**Q: Can I get key bindings? I need a shortcut for this wonderful timesaver!**

A: Of course! Your fingers shall not be denied their favorite key combinations. Check the [Key Bindings](#key-bindings) section to set your own shortcut.

**Q: Is the plugin compatible with different Sublime Text versions and operating systems?**

A: Yes, the Close All without Confirmation plugin is designed to be compatible with Sublime Text 3 and Sublime Text 4 on Windows, macOS, and Linux. If you encounter any compatibility issues, please report them on the GitHub repository.

**Q: I want to help make this plugin even more awesome. Can I contribute?**

A: Absolutely! Contributions and suggestions are always welcome! Feel free to fork the repository, make changes, and submit pull requests. You can also report issues or request new features on GitHub to help make this plugin the best it can be.

## License

MIT License
