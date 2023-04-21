#!/bin/bash
# Downloads all the GSOD data

for i in {1980..2021}
do
	echo "Downloading $i..."
	mkdir $i
	cd $i
	curl https://www.ncei.noaa.gov/data/global-summary-of-the-day/archive/$i.tar.gz --output $i.tar.gz
	tar -xf $i.tar.gz
	rm -f $i.tar.gz
	cd ..
done
