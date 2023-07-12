#!/bin/bash

for f in */index.md;
do
	g="$(dirname $f)"
	echo "$g"

	echo head $f
	head $f

	sed -i '' '1s;^;---\nlayout: default_sparse\ntitle: The British Machine Vision Conference (BMVC)\npermalink: /bmvc/'$g'/index\n---\n\n;' $f

	sed -i '' 's;(\(.*\.pdf\));({{ site.archive_url }}\/bmvc\/'$g'\/\1);g' "$f"

	#sed -n 's;(\(.*\.html\));(https:\/\/www.bmva-archive.org.uk\/bmvc\/'$g'\/\1);gp' "$f"

	echo head $f
	head $f

	echo "\n\n"
done

