#!/bin/bash

input_file="NAVALL.txt" #this file has the contents of the text file given 
output_file="output.tsv" #this stored only the Scheme name and asset value fields

# storing Scheme Name and Asset Value fields only in tsv file
awk -F';' 'BEGIN {OFS = "\t"} NR > 1 {print $4, $5}' "$input_file" > "$output_file"


