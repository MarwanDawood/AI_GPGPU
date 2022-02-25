#!/bin/bash

read -p "get the source projects from Github (y/n)?" choice
if  [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
git clone https://github.com/elorimer/rpi-playground

#QPU assembler
git clone https://github.com/hermanhermitage/videocoreiv-qpu
fi

pushd rpi-playground/QPU/assembler
make
chmod 777 qpu-assembler
cp qpu-assembler ../helloworld


pushd ../helloworld
./qpu-assembler -o helloworld.bin < helloworld.asm

#making a carachter node device to communicate IPC with the GPU through mailboxes found in mailbox.h in linux OS
mknod char_dev c 249 0
make
ls -al

read -p "do you want to execute the final file (y/n)?" choice
if  [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
./helloworld helloworld.bin 249 
fi
