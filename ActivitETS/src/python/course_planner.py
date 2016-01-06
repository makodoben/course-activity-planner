#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET


class MoodleQuiz():
    """Describes a MoodleQuiz with basic information"""
    def __init__(self, path):
        activity = ET.parse(os.path.join(path, 'quiz.xml')).getroot()

        if len(activity) != 1:
            raise Exception('An activity can only have one quiz.')
        self.quiz = activity[0]

    def __getitem__(self, k):
        if k == 'id':
            return self.quiz.attrib[k]
        return self.quiz.find(k).text


class MoodleCourse():
    """Describes a complete moodle course from an archive on the disk"""
    def __init__(self, moodle_archive_path):
        self.path = moodle_archive_path
        self.activities_path = os.path.join(self.path, 'activities')

        if not os.path.isdir(self.activities_path):
            raise Exception('Invalid directory')

    def get_quizes(self):
        activities = os.listdir(self.activities_path)
        return [f for f in activities if f.startswith('quiz')]

    def get_quiz_by_module_id(self, module_id):
        """Gets a quiz from it's ID"""
        quizes = self.get_quizes()

        for quiz_path in quizes:
            if quiz_path == 'quiz_%s' % module_id:
                return MoodleQuiz(os.path.join(self.activities_path, quiz_path))


def main():
    pass

if __name__ == "__main__":
    main()
