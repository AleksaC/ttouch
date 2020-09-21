# ttouch

Create files from templates.

## About 📖
Very often I find myself creating files that almost always have certain contents
(e.g. contact section in README files, general formatting in pre-commit config etc.)
The way I usually do that is by first creating the file and then finding and copying
the appropriate contents from some of my other projects. Because I do this so often
I decided to streamline the process by putting a bunch of such files in a directory
and create a script that copies them to the specified location. Think of it as `touch`
that creates a file according to some template, which is why it was named `ttouch`.
Later on, I learned that the purpose of `touch` is to change file timestamps and
this script doesn't do that so the name might be a bit misleading.

## Usage
```
ttouch foo/bar/baz
```
The script will look for the file named `baz` in the templates directory. If the file
is there it will be copied to `foo/bar/` and if it's not an empty file will be created.

## Setup ⚙️
There are two ways to install the script. You can install it using pip
(you need to use python 3):
```shell script
pip install git+https://github.com/AleksaC/ttouch.git@master
```
The other way is to download the script and put it in a directory on path
(e.g. `/usr/local/bin`):
```shell script
wget -O /usr/local/bin/ttouch "https://raw.githubusercontent.com/AleksaC/ttouch/master/ttouch.py"
chmod +x /usr/local/bin/ttouch
```

### Shell completions
Download the shell completions script:
```shell script
mkdir -p ~/.ttouch
wget -O ~/.ttouch/shell_completions.sh "https://raw.githubusercontent.com/AleksaC/ttouch/master/shell_completions.sh"
```
Completions only work for `bash` and `zsh`, they may work on other shells with
slight modifications but I've never used them and didn't bother looking it up.
To have the shell completions whenever you open your shell add the following line
to your `~/.bashrc` if you're using `bash` or `.zshrc` if using `zsh`:
```shell script
source ~/.ttouch/shell_completions.sh
```

### Templates
To use files as templates just put them in `~/.templates` directory. You can also
use another directory for your templates but you need to specify it using
`TTOUCH_TEMPLATES_DIR` environment variable.

## License ⚖️
[![license](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/AleksaC/ttouch/blob/master/LICENSE)

## Contact 🙋‍♂️
- [Personal website](https://aleksac.me)
- <a target="_blank" href="http://twitter.com/aleksa_c_"><img alt='Twitter followers' src="https://img.shields.io/twitter/follow/aleksa_c_.svg?style=social"></a>
- aleksacukovic1@gmail.com
