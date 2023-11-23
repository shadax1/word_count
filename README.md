# Word Count
Sublime Text plugin written in Python that counts specific words, given by the user, from text or a file.

## How to use?
From the Command Palette:

- `Count Specific Words` opens a panel on the right where the user can then enter words to be counted,
- `Copy Word Counters` from that same panel, copies all words and their counters into the clipboard,
- `Sort Words By Counters` sorts all words in an ascending or descending order based on the counters.

![cp](images/command_palette.png "Command Palette screenshot")

Here is a brief demo:

![demo](images/demo.gif "demonstration")

## Ideas/Improvements/Issues
The execution for this plugin isn't really the best but it does the job for me at the moment.

Current limitations/issues and things I want to improve:

- counting in a large file is quite demanding in terms of cpu
- make it so it doesn't recount after a sort
