import sublime
import sublime_plugin

import os
import functools


class EnhancedNewFileAtCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
        self.window.show_input_panel("File Name:", "", 
            functools.partial(self.on_done, dirs[0]), None, None)

    def on_done(self, dir_name, file_name):
        view = self.window.new_file()
        view.retarget(os.path.join(dir_name, file_name))
        view.run_command("save")


class NewFileEventListener(sublime_plugin.EventListener):
    def on_window_command(self, window, cmd, args):
        if cmd == "new_file_at":
            return ("enhanced_new_file_at", args)