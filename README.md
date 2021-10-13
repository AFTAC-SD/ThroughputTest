# influx-stress
This program is designed to let the user test write limits to an influxdb.  It is setup by default to look for an internally hosted influxdb on port 8086.  It will write to a new database called 'stress'.  

For pulling this in, inside of grafana, you need to change the database name in the database source page, to read 'stress'.  This should immediately turn on the data in the panels for viewing.

# General
The stress program writes multiple tags under a single measurement called 'ctr'.  Even though these are separate tags, the architecture appears to stitches them back together for viewers like grafana.  This splitting into different 'series' is something that can be controlled at the CLI for influx-stress, so you are able to see the performance difference between 1 series (what most people use for a measurement) and some other larger value (100,000 in the case of 2M samples per second).

# for installing on arm64 devices, pull the program by running:
git clone https://go.googlesource.com/go goroot

go into the src folder and run:
./influx-stress insert -r 1m --pps 1000000

where 1m is the duration of 1 minute, can be adjusted to secounds, hours, days as well
&
pps sets the points per second to test

# for installing on x86 devices, install go, and then run:
go get -v github.com/influxdata/influx-stress/cmd/...
