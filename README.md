# Word Count
Sublime Text plugin written in Python that counts specific words, given by the user, from text or a file.

## How to use?
From the Command Palette:
- `Count Specific Words` opens a panel on the right where the user can then enter words to be counted,
- `Copy Word Counters` from that same panel, copies all words and their counters into the clipboard,
- `Sort Words By Counters` sorts all words in an ascending or descending order based on the counters.

![cp](screenshots/command%20palette.png "Command Palette screenshot")

Here is a brief demo:

https://github.com/shadax1/word_count/assets/25485011/67c8bab3-d796-465d-898c-0539731627c0

## Motivation
After almost a decade of using Sublime Text, I decided to finally try writing a plugin for a feature I always needed but wasn't able to find in the current package list.
I watched a few of OdatNurd's [youtube videos](https://www.youtube.com/playlist?list=PLGfKZJVuHW91zln4ADyZA3sxGEmq32Wse) to get started as well as google search (a lot) and use Sublime Text's [forum](https://forum.sublimetext.com/).
I also followed FichteFoll's [suggestions](https://github.com/wbond/package_control_channel/pull/8836) in order to improve the plugin's behavior.

## Ideas/Improvements/Issues
The execution for this plugin isn't really the best but it does the job for me at the moment.

Current limitations/issues and things I want to improve:
- counting in a large file is quite demanding in terms of cpu
- make it so it doesn't recount after a sort
