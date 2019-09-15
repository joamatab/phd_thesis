#!/bin/bash

for i in $(ls *.eps | sed -e 's/\.[a-zA-Z]*$//')

do
	epspdf "$i".eps "$i".pdf

done
