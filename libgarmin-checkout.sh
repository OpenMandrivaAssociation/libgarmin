#!/bin/bash
# This script checkout the source from libgarmin.
# 
# libgarmin-checkout.sh
VERSION=dev
DATE=20090212
REVISION=320
VCS=svn
NAME=libgarmin
rm -rf $NAME-$VERSION
svn export -r $REVISION http://$NAME.svn.sourceforge.net/svnroot/$NAME/$NAME/$VERSION $NAME-$DATE
tar -cjvf $NAME-$DATE$VCS.tar.bz2 $NAME-$DATE --exclude=.$VCS
rm -rf $NAME-$DATE
