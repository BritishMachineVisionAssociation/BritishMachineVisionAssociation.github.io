#!/bin/bash

# for f in *.html; 
# do 
# 	sed -i '' 's|href="\(.*\.pdf\)"|href="https://bmva-archive.org.uk/bmvc/1987/\1"|g' "$f"; 
# done

for f in */index.md;
do
	g="$(dirname $f)"
	echo "$g"

	for h in $g/*.html;
	do
		echo $h

		sed -i '' 's;href="\(.*\.pdf\)";href="https:\/\/bmva-archive.org.uk\/bmvc\/'$g'\/\1";g' $h
	done
done