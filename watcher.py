#!/usr/bin/env python
 
#Timestamp it
timestamp() {
  echo date +"%T"
}
#Infinite loop
while :
do
        if [ -z "$(pgrep PROCNAMEHERE)" ]
        then
                echo "The PROCNAMEHERE is down as of " $(date +%m%d%Y%T)
                echo "PROCNAMEHERE went down!" $(date +%m%d%Y%T) > log$(date +%m%d%Y%T).log
                exec /execute/thing/start.sh
                sleep 120
        else
                sleep 30
                clear
                echo "The PROCNAMEHERE is up as of " $(date +%m%d%Y%T)
        fi
done

#Dirty PY  by illblew
