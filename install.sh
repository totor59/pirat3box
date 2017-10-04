#!/bin/sh

mkdir uploads
mkdir uploads/audio
mkdir uploads/video
mkdir uploads/img
mkdir uploads/others
sudo chown -R www-data:www-data uploads/
sudo chmod -R 777 uploads/
