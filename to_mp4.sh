#!/bin/bash

DIR=$1
cd "$1"

for FILE in *
do
	NAME="${FILE%.*}"
	EXT="${FILE##*.}"
	if [ "$EXT" = "mp4" ]
	then
		continue
	fi
	ffmpeg -i "$FILE" -codec copy "$NAME.mp4"
	rm "$FILE"
done

