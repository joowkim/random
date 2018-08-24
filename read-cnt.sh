Line=0
Line=`zcat $1 | wc -l`
echo $1 $((Line/4)) >> read.cnt.log
