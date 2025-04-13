#!/usr/bin/sh 
printf "\033c\033[43;30m\ndownload base commands"
mkdir source
git clone git://sourceware.org/git/binutils-gdb.git ./source
