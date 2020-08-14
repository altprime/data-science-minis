### Magic Commands
Jupyter notebooks have some nifty features called magic commands. There are a ton of commands out there but I'll inlcude just the few that I find myself using the most and I reckon these will come in handy more often than others. You can see how they actually work in the notebook attached.

1. %lsmagic<br>
This will allow you to list all the magic commands available for jupyter notebooks.
2. %who<br>
There are so many times when I completely forget which variables I have used and scrolling 200 blocks is just not convenient. This function lists all _global_ variables throughout the notebook.
3. %%writefile <filename>.py<br>
This command will convert the code block in which it was written into a python file. 
4. LaTeX<br>
There were times when I had to submit ipynb files as my assignment submissions and we were required to explain everything. That is when I came across the fact that writing math foremulae in markdown mode between two $ signs will conver the block in to LaTeX format. This eventually became my default way to write formulae in notebooks.
5. %pastebin <filename>.py<br>
There are times when I ask people for help on my code. Sure stackoverflow is your go-to for every coding query but sometimes I also ask folks over at reddit. Either way, in order to share code with people the best way is provide them with a link to your code. What this command does is that it takes the contents of an _existing_ python file in your _working directory_ and gives you a Pastebin link, which you can share all over the internet. Comes in handy if the code is too big and inconvenient to paste directly on forums.

Feel free to search for more magic commands I'm sure there may be some particulary suited for your use case.
