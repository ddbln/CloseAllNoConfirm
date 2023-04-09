# CloseAllNoConfirm.py
# A Sublime Text plugin to close all files (saved and unsaved) without confirmation
# Copyright (c) 2023 Dirk Dassow

import sublime
import sublime_plugin

class CloseAllWithoutConfirmCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings("CloseAllNoConfirm.sublime-settings")
        ask_before_closing = settings.get("ask_before_closing", False)

        if ask_before_closing:
            if sublime.ok_cancel_dialog("Close all files and discard unsaved changes?", "Close All"):
                self.close_all_files()
        else:
            self.close_all_files()

    def close_all_files(self):
        for window in sublime.windows():
            for view in window.views():
                view.set_scratch(True)
            window.run_command("close_all")