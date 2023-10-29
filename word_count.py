import sublime
import sublime_plugin


class WordCountCommand(sublime_plugin.WindowCommand):
    def run(self):
        if self.window.num_groups() != 2: #make the layout have 2 panels if not already the case
            self.window.run_command('set_layout', 
                {
                    "cols": [0.0, 0.5, 1.0],
                    "rows": [0.0, 1.0],
                    "cells": [[0,0,1,1], [1,0,2,1]]
                })
        self.window.focus_group(1)
        new_file = self.window.new_file()
        new_file.set_name("Word Count")
        new_file.run_command('insert',
                            {'characters':
                             'Whole word (0: no / 1: yes): 0\n'+
                             'Case sensitive (0: no / 1: yes): 0\n'+
                             'Enter words to count in the next lines:\n\n'})

class WordCountEventListener(sublime_plugin.EventListener):
    view_target = None
    def on_modified(self, view):
        if view.window().num_groups() == 2 and view.window().active_view_in_group(1).name() == "Word Count":
            self.view_target = view.window().active_view_in_group(0)
            view_word_count = view.window().active_view_in_group(1)

            view_word_count.erase_phantoms("word_count")

            region = sublime.Region(0, view_word_count.size())
            file_content = view_word_count.substr(region)
            lst_words = file_content.split("\n")

            flags = 0
            if lst_words[0][-1] == "1":
                flags |= sublime.WHOLEWORD
            if lst_words[1][-1] == "0":
                flags |= sublime.IGNORECASE

            i = 4 #offset
            for word in lst_words[4:]: #slicing the list to skip the first 3 lines
                if len(word) != 0:
                    occurences = self.view_target.find_all(word, flags)
                    #print(f"word => {word} shows up {len(occurences)} times")
                    #add phantom per line thanks to the i offset
                    view_word_count.add_phantom ("word_count",
                                                 sublime.Region(view_word_count.text_point(i, 0), view_word_count.text_point(i, 0)),
                                                 f"{len(occurences)}",
                                                 sublime.LAYOUT_BLOCK) #LAYOUT_INLINE LAYOUT_BLOCK LAYOUT_BELOW
                    i += 1

    def on_activated(self, view):
        if view.window().active_view_in_group(0) != self.view_target:
            self.view_target = view.window().active_view_in_group(0)
            self.on_modified(view)
