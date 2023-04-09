# CloseAllNoConfirm

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
4. Search for `CloseAllNoConfirm` and select it from the list to install.

### Manual Installation

1. Download or clone this repository: `https://github.com/ddbln/CloseAllNoConfirm`
2. Open Sublime Text and click on `Preferences > Browse Packages...` or `Settings > Browse Packages...` to open the packages directory.
3. Copy the entire `CloseAllNoConfirm` folder into the packages directory.

## Usage

### Command Palette

You can trigger the `CloseAllNoConfirm` command using the Command Palette. Press `Shift+Command+P` (Mac) or `Shift+Ctrl+P` (Windows/Linux) to open the Command Palette, then type "CloseAllNoConfirm" (Sublime Text autocompletes) and press Enter.

### Key Bindings

By default, CloseAllNoConfirm does not add key bindings. However, you can easily set up custom key bindings by following these steps:

1. In Sublime Text, click on `Preferences > Browse Packages` or `Settings > Browse Packages` to open the packages folder.
2. Locate the `CloseAllNoConfirm` folder and open the `Default.sublime-keymap` file.
3. Uncomment the suggested key bindings for your platform and modify them as needed.
4. Save the file to apply your changes.

**Or, alternatively:**

1. Open the command palette (Ctrl+Shift+P on Windows/Linux, Cmd+Shift+P on macOS).
2. Type "Preferences: Key Bindings" and press Enter.
3. Add the following key binding to the right-hand pane (user key bindings), adjusting the keys as desired:

```json
{
    "keys": ["ctrl+alt+shift+w"],
    "command": "close_all_without_confirm"
}
```

## Customization

### Optional Confirmation Prompt

By default, this plugin will close all unsaved windows without any confirmation. However, if you want to enable a single confirmation prompt before closing all unsaved windows, you can change the `ask_before_closing` setting in the `CloseAllNoConfirm.sublime-settings` file:

```json
{
    "ask_before_closing": true
}
```

To access the settings file, in Sublime Text, simply go to `Settings` or `Preferences` and then choose `> Package Settings > CloseAllNoConfirm Settings`.

## Frequently Asked Questions

**Q: Does the plugin only close unsaved files or all files?**

A: The CloseAllNoConfirm plugin closes all files, including both unsaved and saved ones. "Unsaved files" is mentioned in the description above, because dealing with multiple confirmation dialogs can quickly become a painful experience. But don’t worry, this plugin has got you covered – it closes all files swiftly and efficiently!

**Q: I can't imagine a scenario in which I would need this... so ...why...?**

A: Let's say you searched and replaced with one click in a dozen or hundreds of files: Saving them all without asking is easy with Sublime Text, but have you ever tried closing them without saving?

**Q: Is there any risk of losing my work when using this plugin?**

A: The plugin is designed for speed and convenience, but of course accidents can happen. If you’re concerned about losing unsaved work, you can enable the optional single confirmation prompt in the [settings](#optional-confirmation-prompt). This way, you’ll get one friendly reminder to save your work before the plugin closes all files.

**Q: Will this plugin slow down my Sublime Text or cause any performance issues?**

A: No, the CloseAllNoConfirm plugin is lightweight and efficient. It should not cause any noticeable performance issues in your Sublime Text environment.

**Q: Can I have key bindings? I need a shortcut for this timesaver!**

A: Of course! Your fingers shall not be denied their favorite key combinations. Check the [Key Bindings](#key-bindings) section to set your own shortcut.

**Q: I want to help make this plugin even more awesome. Can I contribute?**

A: Absolutely! Contributions and suggestions are always welcome! Feel free to fork the repository, make changes, and submit pull requests. You can also report issues or request new features on GitHub to help make this plugin the best it can be.

## License

MIT License
