# DNA-Program.py

# Motivation
The goal of this program is to have the user input a DNA string and have the complementary printed out. For example if the user were to print CTTAGTTC the program would print out GAATCAAG.

## How to run the program on a Mac
If you are a Mac user (like me) there are a couple of things needed in order to run the program. First save the program in a file. Remember to save it as name.py (name is just my example you can call it whatever you want as long as you have py at the end to indicate this is a python program). After you have saved the program place it on your desktop, the reason I say desktop is because (personally) I feel like it is easier to access. Once you have done that open up your terminal and type python./name.py. If your code is correct it should run and everything should be good to go.

## How to run the program on Windows
I realize not everyone is a Mac user, so here's how you run the program on Windows. The saving method is the same as the Mac you must add a py at the end to indicate to the operating system that this is a python program. In order to call the program you must do so on the Command Prompt. Once that is open you must pass the path of the program as an argument to the python interpreter. C:\Python27\python.exe C:\Users\Username\Desktop\my_python_script.py. Notice the new variable introduced python.exe. You must add the python.exe to your PATH Enviromental Variable. To learn more about PATH Enviromental Variable click **[here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/)**. One final important thing to notice is when you run your program you will notice Windows generates two executables. One is python.exe and the other is pythonw.exe. If you want Command Prompt to pop up while your program is running use python.exe otherwise use pythonw.exe. That is the only difference. 

### Bugs
The only bug in this program is when the user inputs an invalid strand. For example if the user enters the strand 'LJK' the output to the program would have to be Please input valid DNA string. However when you run this program when the user enters 'LJK' the output is Please input valud DNA string three times. If you were the add one more incorrect letter to the strand the output would increase by one. Although the program still does work it is quite annoying because it would be better if it printed once that the user input was invalid. 
