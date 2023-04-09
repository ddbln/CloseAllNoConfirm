# CloseAllNoConfirm

Effortlessly close all files in Sublime Text without being interrupted by confirmation dialogs! This plugin is ideal for those who want to swiftly close multiple unsaved files without needing to confirm each one individually. Optionally, you can enable a single confirmation prompt before closing all files.

## Features

- Close all files without confirmation dialogs.
- Optional single confirmation prompt for cautious users.
- Customizable key bindings.
- Also accessible via Command Palette.

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

### Key Bindings

By default, the following key bindings are set to close all unsaved windows:

- Windows/Linux: `Ctrl+Alt+Shift+W`
- macOS: `Cmd+Alt+Shift+W`

To close all unsaved windows without confirmation dialogs, simply press the corresponding key combination.

### Command Palette

Alternatively, you can trigger the `CloseAllNoConfirm` command using the Command Palette. Press `Shift+Command+P` (Mac) or `Shift+Ctrl+P` (Windows/Linux) to open the Command Palette, then type "CloseAllNoConfirm" and press Enter.

## Customization {#customization}

### Key Bindings

If you want to change the default key bindings, go to `Preferences > Key Bindings` or `Settings > Key Bindings` in Sublime Text, and add a new key binding entry to your user key bindings file, like this:

```json
{
    "keys": ["your_key_combination"],
    "command": "close_all_without_confirm"
}
```

Replace "your_key_combination" with your desired key combination.

### Optional Confirmation Prompt {optional-confirmation-prompt}

By default, this plugin will close all unsaved windows without any confirmation. However, if you want to enable a single confirmation prompt before closing all unsaved windows, you can change the `ask_before_closing` setting in the `CloseAllNoConfirm.sublime-settings` file:

```json
{
    "ask_before_closing": true
}
```

To access the settings file, go to `Settings`or `Preferences ` `> Package Settings > CloseAllNoConfirm > Settings` in Sublime Text.

## Frequently Asked Questions

**Q: Does the plugin only close unsaved files or all files?**

A: The CloseAllNoConfirm plugin closes all files, including both unsaved and saved ones. "Unsaved files" is mentioned initially in the description because that’s often the primary pain point users experience when dealing with multiple confirmation dialogs. But don’t worry, this plugin has got you covered – it closes all files swiftly and efficiently!

**Q: Is there any risk of losing my work when using this plugin?**
A: The primary purpose of this plugin is to close all files without confirmation dialogs, which speeds up the process of closing multiple files. However, if you have unsaved changes in any files, you might lose them when using this plugin. It's always a good practice to save your work before closing files. For cautious users, you can enable the optional single confirmation prompt in the [settings](#optional-confirmation-prompt), which will ask you once before closing all files.

**Q: Will this plugin slow down my Sublime Text or cause any performance issues?**

A: No, the CloseAllNoConfirm plugin is lightweight and efficient. It should not cause any noticeable performance issues in your Sublime Text environment.

**Q: What if I accidentally close all files and lose my unsaved work?**

A: The plugin is designed for speed and convenience, but of course accidents can happen. If you’re concerned about losing unsaved work, you can enable the optional single confirmation prompt in the settings. This way, you’ll get one friendly reminder to save your work before the plugin closes all files.

**Q: Can I customize the key bindings? I have fingers trained for specific shortcuts!**

A: Of course! Your fingers shall not be denied their favorite key combinations. Simply head over to `Preferences > Key Bindings` in Sublime Text and set up your custom key binding for the CloseAllNoConfirm command. Check the [Customization](#customization) section for more details.

**Q: I want to help make this plugin even more awesome. Can I contribute?**

A: Absolutely! Contributions and suggestions are always welcome! Feel free to fork the repository, make changes, and submit pull requests. You can also report issues or request new features on GitHub to help make this plugin the best it can be."

## License

MIT License
