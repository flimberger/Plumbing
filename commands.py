import os
import sublime
import sublime_plugin
import subprocess

from os.path import dirname


debug = True


def _get_homedir():
    p = os.environ['HOME']
    if not p and sublime.platform() == 'windows':
        p = os.environ['USERPROFILE']
    if not p:
        p = '/'
    return p


def _get_working_dir(view):
    filename = view.file_name()
    if filename == '':
        return _get_homedir()
    return dirname(filename)


class PlumbCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        if len(sels) == 0 or len(sels[0]) == 0:
            self.view.window().status_message('Nothing selected')
        else:
            wdir = _get_working_dir(self.view)
            data = self.view.substr(sels[0])
            # Using plumb(1) because 9p(1) fails with
            #
            #     9p: fsopen send: permission denied
            with subprocess.Popen(['9', 'plumb', '-s', 'subl', '-w', wdir, data], close_fds=True, stderr=subprocess.PIPE) as p:
                if p.returncode != 0:
                    emsg = p.stderr.read()
                    msg = 'Failed to plumb "' + data + '"'
                    if emsg != '':
                        msg += ': ' + emsg.decode('UTF-8')
                    self.view.window().status_message(msg)


class EditPlumbingCommand(sublime_plugin.WindowCommand):
    def run(self):
        home = _get_homedir()
        v = self.window.open_file(home + '/lib/plumbing')
