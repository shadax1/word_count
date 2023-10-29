# word_count
Sublime Text plugin written in Python that counts specific words, given by the user, from text or a file.

## How to use?
By simply using `Count Specific Words` from the command palette, a panel on the right will show up and the user can then enter words to be counted. It's also possible to copy all words with their counters into the clipboard and sort words in an ascending or descending order from the command palette.

![cp](https://github.com/shadax1/word_count/blob/main/screenshots/command%20palette.png?raw=true)

Here is a brief demo:

https://github.com/shadax1/word_count/assets/25485011/6fec7a30-31fb-44aa-89d6-a0b841cd426c

## Misc
After almost a decade of using Sublime Text, I decided to finally try writing a plugin for a feature I always needed but wasn't able to find in the current package list.
I watched a few of OdatNurd's [youtube videos](https://www.youtube.com/playlist?list=PLGfKZJVuHW91zln4ADyZA3sxGEmq32Wse) to get started as well as google search (a lot) and use Sublime Text's [forum](https://forum.sublimetext.com/).
I also followed FichteFoll's [suggestions](https://github.com/wbond/package_control_channel/pull/8836) in order to improve the plugin's behavior.

## Ideas/Improvements/Issues
The execution for this plugin isn't really the best but it does the job for me at the moment.

Current limitations/issues and things I want to improve:
- typing in the command palette triggers `on_modified_async` which can be annoying with large files
- counting in a large file is quite demanding in terms of cpu
- make it so it doesn't recount after a sort
