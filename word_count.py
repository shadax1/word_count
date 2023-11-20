import sublime
import sublime_plugin

clipboard = ""

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
    def __init__(self):
        self.view_target = None

    def on_modified_async(self, view):
        if view.window() != None:
            if view.window().num_groups() == 2 and view.window().active_view_in_group(1).name() == "Word Count" and view.settings().get('is_widget') == None:
                global clipboard
                self.view_target = view.window().active_view_in_group(0) #view from which we count words
                view_word_count = view.window().active_view_in_group(1) #view in which we will insert counters

                #get all lines from the word_count view
                region = sublime.Region(0, view_word_count.size())
                file_content = view_word_count.substr(region)

                #check flags
                lst_words = file_content.split("\n")
                flags = 0
                if lst_words[0][-1] == "1":
                    flags |= sublime.WHOLEWORD
                if lst_words[1][-1] == "0":
                    flags |= sublime.IGNORECASE

                #count words from target view, insert phantoms in word_count view and update clipboard string
                i = 4 #offset
                clipboard = ""
                self.phantom_set = sublime.PhantomSet(view_word_count, 'phantom_set')
                self.phantoms = []
                for word in lst_words[4:]: #slicing the list to skip the first 3 lines
                    if len(word) != 0:
                        occurences = self.view_target.find_all(word, flags)
                        #print(f"word => {word} shows up {len(occurences)} times")
                        self.phantoms.append(sublime.Phantom(sublime.Region(view_word_count.text_point(i, len(word))),
                                            ":\t" + "{}".format(len(occurences)),
                                            sublime.LAYOUT_INLINE))
                        clipboard += "{}\t{}\n".format(word, len(occurences))
                        i += 1
                self.phantom_set.update(self.phantoms)

    def on_activated_async(self, view): #tab has changed
        if view.window() != None:
            if view.window().active_view_in_group(0) != self.view_target:
                self.view_target = view.window().active_view_in_group(0) #update the target view object to the new one
                self.on_modified_async(view) #retrigger the count

class CopyWordCountersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.name() == "Word Count":
            sublime.set_clipboard(clipboard)
        else:
            self.view.set_status("Charcode", "[WordCount] You must use the Count Specific Words command first!")

class SortWordsByCountersAscendingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.name() == "Word Count":
            sort_words("ascending", self.view, edit)
        else:
            self.view.set_status("Charcode", "[WordCount] You must use the Count Specific Words command first!")

class SortWordsByCountersDescendingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.name() == "Word Count":
            sort_words("descending", self.view, edit)
        else:
            self.view.set_status("Charcode", "[WordCount] You must use the Count Specific Words command first!")

def sort_words(order, view, edit):
    #create a list of lists to easily sort everything accordingly
    lst_words = []
    for item in clipboard.split("\n"):
        if len(item) != 0:
            lst_words.append([item.split("\t")[0], item.split("\t")[1]])
    
    #sort
    if order == "ascending":
        lst_words.sort(key=lambda x: int(x[1]))
    else: #descending
        lst_words.sort(key=lambda x: int(x[1]), reverse=True)
    
    #store the sorted words back into a new string
    sorted_words = ""
    for word in lst_words:
        sorted_words += "{}\n".format(word[0])

    #replace the existing content of the view with the newly created string
    region = sublime.Region(107, len(view)) #107 characters to leave the settings lines intact
    view.replace(edit, region, sorted_words)
