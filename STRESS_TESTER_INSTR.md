# for installing on arm64 devices, pull the program by running:
git clone https://go.googlesource.com/go goroot

go into the src folder and run:
./influx-stress insert -r 1m --pps 1000000

where 1m is the duration of 1 minute, can be adjusted to secounds, hours, days as well
&
pps sets the points per second to test

# for installing on x86 devices, install go, and then run:
go get -v github.com/influxdata/influx-stress/cmd/...
