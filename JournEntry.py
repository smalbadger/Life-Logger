import sys
import csv

class Jentry:
    def __init__(self,id,date="00/00/0000", time="00:00:00", header=None, body=None, tags=''):
        self._id = str(id)
        self._date = str(date)
        self._time = str(time)
        self._header = str(header)
        self._body = str(body)
        self._tags = str(tags)

    #----GETTERS----
    def get_entry_id(self):
        return self._id
    def get_date(self):
        return self._date
    def get_header(self):
        return self._header
    def get_body(self):
        return self._body
    def get_tags(self):
        return self._tags

    #----SETTERS----
    def set_date(self, date):
        self._date = date
    def set_header(self, header):
        self._header = header
    def set_body(self, body):
        self._body = body
    def add_tag(self, tag):
        self._tags.append(tag)
    def remove_tag(self, tag):
        if tag in tags:
            tags.remove(tag)

    def write_entry_to_file(self):
        jour_file = csv.writer(open('journal.csv', 'a'))
        jour_file.writerow((self._id,self._date,self._time,self._header,self._body,self._tags))

    def __str__(self):
        _str = self._date + '\t' + self._time
        _str += "\n" + self._header + ":\n" + self._body + "\n"
        return _str
