from .Homework import Homework
import os


class Homework3(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["1.1.0"]

        data_files = {
            "1.1.0": [
                "bio462_hw3_ans.txt",
                "bio462_hw3_hint.txt"
            ],
        }

        super().__init__(hw_number="hw3", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        # need to reference file of answer key and hints
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]

            if file_name == "bio462_hw3_ans.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "bio462_hw3_hint.txt":
                self.hintDict = self.parseHints(file_path)
