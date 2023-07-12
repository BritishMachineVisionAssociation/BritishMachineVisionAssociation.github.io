#!/bin/bash

for f in *.html; 
do 
	sed -i '' 's|href="\(.*\.pdf\)"|href="https://bmva-archive.org.uk/bmvc/1987/\1"|g' "$f"; 
done

