# asciitable
Small Python3 script with no dependencies that prints the ASCII table like asciitable.com.

![demo](./demo.png)

## Why? 

I got bored of going to [asciitable.com](http://www.asciitable.com/) everytime I needed to look at a couple of ASCII characters.

## How to Run

Run it with ```./asciitable.py``` or ```python3 asciitable.py```

Check the options here:
```
asciitable.py - ASCII Table Printer

                -h/--help - Print this help
                -nc/--no-colour - Disable Colours
                -c/--colours [tablecolour] [textcolour]
                        Choose the colours for the table. (Default: blue green)
                        (magenta, blue, green, yellow, red, cyan, black, white)
```

You can also copy it to `/usr/bin` like:

`sudo cp asciitable.py /usr/bin/asciitable`

Or you could make an alias for it using your preferred shell by adding this line to the rc file (.bashrc for example):

`alias asciitable="/path/to/asciitable.py"`


Go nuts with it, enjoy 😃!

Contributions are more than welcome, as usual.
