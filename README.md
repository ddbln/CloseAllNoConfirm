# Force Close All Files

Force close all files in Sublime Text — instantly discard unsaved changes, no confirmation dialogs! This plugin lets you force close all open files (saved and unsaved) without being repeatedly interrupted by save prompts.

## Features

- Force close all files without confirmation dialogs.
- Option to close files only in the currently active window, perfect for those working with multiple projects.
- Accessible via the Command Palette.
- Easy-to-activate key bindings (instructions provided).
- For cautious users: By default, "Force Close All Files" shows you a prompt before closing. However, you can disable this prompt in the settings to skip it entirely.

## Installation

### Via Package Control

1. Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
2. Open the command palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
3. Type `Package Control: Install Package` and press Enter.
4. Search for `Force Close All Files` and select it from the list to install.

### Manual Installation

1. Download or clone this repository: `https://github.com/ddbln/CloseAllNoConfirm`
2. Open Sublime Text and click on `Preferences > Browse Packages...` or `Settings > Browse Packages...` to open the packages directory.
3. Copy the entire folder into the packages directory.

## Usage

When you trigger the `Force Close All Files` command using the Command Palette or your custom key binding, you will see a quick panel with two options: "Force close all files in all windows" and "Force close files in this window". You can use the arrow keys to select your desired option and press Enter to confirm.

### Command Palette

You can trigger the command using the Command Palette. Press `Shift+Command+P` (Mac) or `Shift+Ctrl+P` (Windows/Linux) to open the Command Palette, then type "close all" or "force close" and press Enter.

### Key Bindings

By default, "Force Close All Files" does not add key bindings. However, you can easily set up custom key bindings by following these steps:

1. In Sublime Text, go to `Preferences` > `Package Settings` > `Force Close All Files` > `Key Bindings - Default`. This will open the default key bindings file for the plugin.
2. Copy the key binding for your platform (Windows, Linux, or macOS) from the default key bindings file.
3. Go to `Preferences` > `Package Settings` > `Force Close All Files` > `Key Bindings - User` to open your user-specific key bindings file.
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

### Disabling the Confirmation Prompt

The plugin offers a customization option that allows you to toggle whether you want a single confirmation prompt before force closing all files. By default, the plugin will ask you once, and you can then choose if you want to force close all files in all windows or just the current one, or cancel.

However, you can easily change this setting to force close all files in all windows without any prompt by setting the following options in your User settings:

```json
{
	"ask_before_closing": false,
	"close_only_active_window": false
}
```

In case you want to only close the active windows' files you can set `close_only_active_window` to `true`.

To access the settings file, in Sublime Text, simply go to `Settings` or `Preferences` and then choose > `Package Settings` > `Force Close All Files` > `Settings`.

## Frequently Asked Questions

**Q: Does the plugin only close unsaved files or all files?**

A: Force Close All Files closes all files, both unsaved and saved, with the main benefit being that you won't be prompted for each unsaved file. Dealing with multiple confirmation dialogs can quickly become a painful experience. But don't worry, this plugin has got you covered.

**Q: Can I choose to close files only in the active window?**

A: Yes, you have the option to close files either in all windows or only in the active window. When you trigger the command, a quick panel will appear with these two options. Simply select your desired option and press Enter to confirm. Note that you can only choose this if the "ask_before_closing" option is turned on (which is by default).

**Q: Can you provide an example of when this plugin would be useful?**

A: Suppose you've searched and replaced a dozen or hundreds of files with a single click: saving them all is easy with Sublime Text and takes just one command (and no questions asked). But: have you ever tried to close them without saving?

**Q: Is there any risk of losing my work when using this plugin?**

A: Although the plugin is designed for speed and convenience, accidents can still occur. That's why, by default, you will receive a single confirmation prompt before action, reminding you that any unsaved changes will be lost. However, if you wish to disable this prompt, you can do so by setting the "ask_before_closing" option to false in the settings.

**Q: Will this plugin slow down my Sublime Text or cause any performance issues?**

A: No, Force Close All Files is lightweight and efficient. It should not cause any noticeable performance issues in your Sublime Text environment.

**Q: Can I get key bindings? I need a shortcut for this wonderful timesaver!**

A: Of course! Your fingers shall not be denied their favorite key combinations. Check the [Key Bindings](#key-bindings) section to set your own shortcut.

## License

MIT License
