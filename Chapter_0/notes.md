# Start Here

If you're reading this, then you are most likely a friend, family member, or other that I have insisted learn Python. In order to get set up for the PY4E course, there are a few steps we have to go through first. For some key concepts and instructions, I have included a hyperlink that provides either additional information, steps, or documentation that might be helpful.

These steps will ensure that we have a proper development environment for not only the course, but for your future programming adventures.

I am advocating for the use of a [UNIX environment](https://ccrma.stanford.edu/guides/planetccrma/Unix_Environment.html). In my opinion, using a UNIX environment can help streamline development by providing a much more robust and efficient platform to construct and deploy your code. By no means is this a requirement, it's simply my recommendation for this tutorial.

## Step 1: Environment (macOS/Linux):

1. If you are using macOS, go ahead and open up the [Terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac). Otherwise, in your Linux machine, navigate to the Command Line Interface (CLI).

2. Read through some of the [CLI commands](https://www.geeksforgeeks.org/basic-linux-commands/). See if you can figure out how to create a folder named "PY4E" on your desktop using only the CLI.
   - (Hint: You will have to use the commands `cd` and `mkdir` to accomplish this)

## Step 1: Environment (Windows):

1. On a Windows machine, a UNIX environment isn't readily available. One of the most straightforward ways to initialize one would be to [install Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command). WSL allows for the quick and easy set up of a Linux environment without the hassle of dealing with virtual machines or dual-booting.

2. Once you have installed WSL, read through some of the [CLI commands](https://www.geeksforgeeks.org/basic-linux-commands/). See if you can figure out how to create a folder named "PY4E" on your desktop using only the CLI.
   - (Hint: You will have to use the commands `cd` and `mkdir` to accomplish this)

## Step 2: Installing Python

1. If you're planning to do this course on macOS, then I suggest following [this article](https://www.geeksforgeeks.org/how-to-install-python-on-mac/#how-to-install-python-3131-on-macos-using-homebrew) for installing Python.

   - If you're planning to do this course on Windows or Linux, enter `sudo apt install python3`. This will install Python.

2. Once Python is installed, run `python3` in the CLI. You shoud now see an output similar to the following:

   `Python 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0] on linux`<br>
   `Type "help", "copyright", "credits" or "license" for more information.`<br>
   `>>> `

## Step 3: Installing Visual Studio Code

1. Visual Studio Code is an Integrated Development Environment, or IDE. An IDE makes it a lot easier to write code since it supports a variety of features, such as auto-complete, version control, and more. [Here](https://code.visualstudio.com/download#) is where you can find the VSCode download link for your specific device.

   - If you're on Windows, also install the WSL extension which can be found in [this article](https://code.visualstudio.com/docs/remote/wsl-tutorial).

2. Once VSCode has been downloaded, navigate to the Extensions tab on the left-hand icon pane. In the search bar that appears near the top left, enter `Python`. Once you find the similarly named extension by Microsoft (it might not be the top result), select it and click install.

3. Once that is installed, we should be ready to write our first line of Python code! Go ahead and close VSCode. From here on out, we will be launching VSCode from the command line.

## Step 4: Hello World

1. Assuming everything went well with the previous steps, we should be ready to make sure everything works! In the CLI, navigate to the "PY4E" folder you created in Step 1.

2. Once you've made it there, type `code .` and press enter. This should launch VSCode inside of our current folder. To check, if we press the first icon on the left-hand pane (it looks like two overlapping files), we should see that we are inside our empty "PY4E" folder once the 'EXPLORER' menu opens. In order to access the CLI in VSCode, navigate to 'Terminal' in the top left, and select 'New Terminal'. You should now have two different ways to view the files and sub-folders of your current folder.

3. This may be getting ahead of ourselves, but lets try to write and run our very first Python script. In 'EXPLORER', right-click and select 'New File'. Let's title it `hello_world.py`.

4. Click on 'hello_world.py' and type `print("Hello, world!")`. Save the file, and click on the awaiting terminal on the bottom of the screen.

5. Enter `python3 hello_world.py` and you should expect to see the following output:<br>
   `Hello, world!`<br>
   Pretty cool, right?!<br>

You are now ready to continue on with the course. I hope you enjoy learning Python, and do amazing things with your newfound programming ability after the tutorial.
