import subprocess
import os.path
import sys

import pytest


def pytest_collect_file(parent, path):
    if path.basename.startswith("test"):
        return ShabangFile(path, parent)


class ShabangFile(pytest.File):
    def collect(self):
        yield ShabangItem(os.path.relpath(self.fspath), self, self.fspath)

class ShabangItem(pytest.Item):
    def __init__(self, name, parent, filename):
        super().__init__(name, parent)
        self.filename = filename

    def runtest(self):
        subprocess.check_call(str(self.filename), stdout=sys.stdout, stderr=sys.stderr, shell=True)
        
    def repr_failure(self, excinfo):
        """ called when self.runtest() raises an exception. """
        if isinstance(excinfo.value, subprocess.CalledProcessError):
            return "\n".join(
                [
                    "execution failed with",
                    "   returncode: %r" % excinfo.value.returncode ,
                ]
            )

    def reportinfo(self):
        return self.fspath, 0, "file: %s" % self.name