#!/bin/bash

timestamp() {
    date +%s
}


TS=$(timestamp)
USER=johnnymusk
HOST=10.0.2.147
DIR=~
ZIPFILE=backup_$TS.zip
BACKUP_PASS=$(~/backups/pass_gen.sh $TS)

zip -r --password $BACKUP_PASS $ZIPFILE ~/Desktop/TVShows
rsync -avz -e "ssh -i ~/.ssh/id_rsa" ./$ZIPFILE $USER@$HOST:$DIR
rm $ZIPFILE

