# CloseAllWithoutConfirm.py
# A Sublime Text plugin to close all files (saved and unsaved) without confirmation
# Copyright (c) 2023 Dirk Dassow

import sublime
import sublime_plugin

class CloseAllWithoutConfirmCommand(sublime_plugin.WindowCommand):
    """
    A Sublime Text command that closes all open files, saved and unsaved, 
    without confirmation or with confirmation, based on the user's preference.
    """

    def run(self):
        ask_before_closing = self.get_setting("ask_before_closing", False)

        if ask_before_closing:
            if sublime.ok_cancel_dialog("Close all files and discard unsaved changes?", "Close All"):
                self.close_all_files()
        else:
            self.close_all_files()

    def get_setting(self, setting_name, default_value=None):
        settings = sublime.load_settings("CloseAllNoConfirm.sublime-settings")
        return settings.get(setting_name, default_value)

    def close_all_files(self):
        for window in sublime.windows():
            for view in window.views():
                view.set_scratch(True)
            window.run_command("close_all")
