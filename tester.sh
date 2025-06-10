#!/bin/bash

# Ask user for the .mus filename
read -p "Enter the name of your .mus file (without extension): " mus_filename

# Check if file exists
if [ ! -f "${mus_filename}.mus" ]; then
    echo "Error: File ${mus_filename}.mus not found!"
    exit 1
fi

echo "Compiling ${mus_filename}.mus..."

# Compile the .mus source to LLVM IR
python3 main.py "${mus_filename}.mus"

# Check if compilation succeeded
if [ ! -f "${mus_filename}.ll" ]; then
    echo "Error: Failed to generate LLVM IR!"
    exit 1
fi

# Compile the C music functions
echo "Compiling personalized functions..."
gcc -c personalized_functions_ubuntu.c -o personalized_functions_ubuntu.o

# Generate object from LLVM IR
echo "Generating object file..."
llc -filetype=obj "${mus_filename}.ll" -o "${mus_filename}.o"

# Link everything
echo "Linking final executable..."
clang "${mus_filename}.o" personalized_functions_ubuntu.o -o "${mus_filename}"

# Check if linking succeeded
if [ ! -f "${mus_filename}" ]; then
    echo "Error: Failed to create executable!"
    exit 1
fi

# Run the generated binary
echo "Executing ${mus_filename}..."
./"${mus_filename}"