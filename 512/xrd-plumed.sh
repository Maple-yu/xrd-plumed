#!/bin/sh

list1="liq gra dia"
list2="4096 13824 32768 6400"

for i in $list2;
do
	echo "running with ${i} atoms"
	for j in $list1;
	do
		echo "analyse the ${j}_N${i}nm.xyz"
		## plumed driver --plumed ./${i}/plumed-${j}.dat --ixyz ./${i}/${j}_N${i}nm.xyz
	done
done
echo "All job done!"