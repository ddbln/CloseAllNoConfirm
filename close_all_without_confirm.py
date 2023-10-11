# CloseAllWithoutConfirm.py
# A Sublime Text plugin to close all files (saved and unsaved) without confirmation
# Copyright (c) 2023 Dirk Dassow

import sublime
import sublime_plugin

class CloseAllWithoutConfirmCommand(sublime_plugin.WindowCommand):
    def run(self):
        ask_before_closing = self.get_setting("ask_before_closing", False)
        close_only_active_window = self.get_setting("close_only_active_window", False)

        if ask_before_closing:
            options = ["Close All in all windows", "Close all in this window", "Cancel"]
            sublime.active_window().show_quick_panel(options, self.on_done)
        else:
            self.close_all_files(close_only_active_window)

    def on_done(self, index):
        if index == 0:
            self.close_all_files(False)
        elif index == 1:
            self.close_all_files(True)
        # If index == 2, do nothing because the user selected "Cancel".

    def get_setting(self, setting_name, default_value=None):
        settings = sublime.load_settings("CloseAllNoConfirm.sublime-settings")
        return settings.get(setting_name, default_value)

    def close_all_files(self, close_only_active_window):
        if close_only_active_window:
            active_window = sublime.active_window()
            self.close_all_files_in_window(active_window)
        else:
            for window in sublime.windows():
                self.close_all_files_in_window(window)

    def close_all_files_in_window(self, window):
        for view in window.views():
            view.set_scratch(True)
        window.run_command("close_all")
