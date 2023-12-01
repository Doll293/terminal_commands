# terminal_commands
This project aims to create alternative command versions for linux terminal commands on Windows. The project is 
available only on Windows.

![GitHub Repo stars](https://img.shields.io/github/stars/Dan-Popescu/terminal_commands)

## Recommendations
It's recommended to use Python 3.6 or above

# How to use
1. Clone this repo on the machine you want  
```git clone https://github.com/Dan-Popescu/terminal_commands.git```
2. Open a command line
3. Navigate to the project's directory in the command line
4. Type ```python src/cmd.py``` on the command line
5. You can type any of the available commands (currently only ```ls``` is available)

# Project Structure
The project is organized as follows:

- `src/`: Contains the source code.
- `src/commands`: Contains folders with source code for each type of command.
- `src/commands/ls` : Contains source code for the command ls
- `cmd.py`: Enter command typing mode.

# How to contribute
We welcome contributions from the community to expand this project and add more Linux commands. 
Here's how you can contribute:

1. Fork the repository  
- Click on Fork 
- Click on Create Fork
2. Clone the forked repository
- Copy the https url
- Clone the repository using the previously copied url :  
```python
git clone <fork repo url>
```
3. Create a branch for your feature or fix  
```py
git checkout -b your-branch-name
```
4. Make your changes and test them locally  
```py
python src/cmd.py
```
5. Commit your changes locally   
```py
git commit -m "Description of your changes"
```
6. Push your changes to the remote forked repository    
```py
git push origin your-branch-name
```  
7. Open pull request with a merge of your forked repository into the original repository 
- Visit your fork on GitHub in a web browser. 
- Switch to the branch you pushed. 
- Click on the "New pull request" button.
- Ensure the base branch is set to the main branch of the original repository, 
and the compare branch is set to your branch. 
- Add a description for your changes.
- Click on the "Create pull request" button.

Your contribution will be reviewed, discussed, and potentially merged into the main project.
Thank you for contributing to making this tool more powerful and useful for the Windows community.

Feel free to open issues to discuss new features, report bugs, or suggest improvements.
We look forward to building a robust and comprehensive project together. Thanks for your collaboration!

## License

This project is licensed under the [MIT License](LICENSE).





