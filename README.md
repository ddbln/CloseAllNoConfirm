# Close All without Confirmation

Effortlessly close all (unsaved and saved) files in Sublime Text without being repeatedly interrupted by confirmation dialogs! This plugin is perfect for those who want to swiftly close multiple unsaved files without needing to confirm each one individually.

## Features

- Close all files without confirmation dialogs.
- Accessible via the Command Palette.
- Easy-to-activate key bindings (instructions provided).
- For cautious users: By default, "Close All without Confirmation" shows you a prompt before closing all files. However, you can disable this prompt in the settings to let the plugin truly live up to its name.

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

By default, "Close All without Confirmation" does not add key bindings. However, you can easily set up custom key bindings by following these steps:

1. In Sublime Text, go to `Preferences` > `Package Settings` > `Close all without Confirmation` > `Key Bindings - Default`. This will open the default key bindings file for the plugin.
2. Copy the key binding for your platform (Windows, Linux, or macOS) from the default key bindings file.
3. Go to `Preferences` > `Package Settings` > `Close all without Confirmation` > `Key Bindings - User` to open your user-specific key bindings file.
4. Paste the key binding you copied from the default key bindings file into your user key bindings file.
5. Make sure to remove the "//" at the beginning of the lines to uncomment the key binding, then save the file.

The key binding should now be enabled and ready to use.

**Suggested Key Bindings**

For macOS you could use e. g. the following suggested key binding:

````json
[
	{
		"keys": ["super+alt+shift+w"],
		"command": "close_all_without_confirm"
	}
]
````

A suggestion for Windows and Linux platforms:

```json
[
	{
		"keys": ["ctrl+alt+shift+w"],
		"command": "close_all_without_confirm"
	}
]
```


## Customization

### Optional Confirmation Prompt

This plugin offers a customization option that allows you to toggle whether you want a single confirmation prompt before closing all files without further confirmation. By default, the plugin will ask you once. However, you can easily change this setting to close all files without any prompt by toggling the following option in your User settings:

```json
{
	"ask_before_closing": false
}
```

To access the settings file, in Sublime Text, simply go to `Settings` or `Preferences` and then choose > `Package Settings` > `Close All without Confirmation` > `Settings`.

## Frequently Asked Questions

**Q: Does the plugin only close unsaved files or all files?**

A: The 'Close All without Confirmation' plugin closes all files, both unsaved and saved, with the main benefit being that you won't be prompted for each unsaved file. Dealing with multiple confirmation dialogs can quickly become a painful experience. But don’t worry, this plugin has got you covered – it closes all files swiftly and efficiently!

**Q: Can you provide an example of when this plugin would be useful?**

A: Suppose you've searched and replaced a dozen or hundreds of files with a single click: saving them all is easy with Sublime Text and takes just one command (and no questions asked). But: have you ever tried to close them without saving?

**Q: Is there any risk of losing my work when using this plugin?**

A: Although the plugin is designed for speed and convenience, accidents can still occur. That's why, by default, you will receive a single confirmation prompt before action, reminding you that any unsaved changes will be lost. However, if you wish to disable this prompt, you can do so by setting the "ask_before_closing" option to false in the settings. By doing so, the plugin will truly live up to its name.

**Q: Will this plugin slow down my Sublime Text or cause any performance issues?**

A: No, the Close All without Confirmation plugin is lightweight and efficient. It should not cause any noticeable performance issues in your Sublime Text environment.

**Q: Can I get key bindings? I need a shortcut for this wonderful timesaver!**

A: Of course! Your fingers shall not be denied their favorite key combinations. Check the [Key Bindings](#key-bindings) section to set your own shortcut.

## License

MIT License
