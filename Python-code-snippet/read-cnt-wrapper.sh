####### wrapper shell file ######
bash read-cnt.sh > read.log
echo
echo $"FileName"	"ReadCount"
cat read.log | sort -k 2 -r
