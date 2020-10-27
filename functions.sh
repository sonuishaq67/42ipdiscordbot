#!/bin/bash
stop_process() {
    process_id=$(ps -ef | grep "bot.py" | cut -b 12-16 | head -n 1)
    kill -9 $process_id
}

run_again() {
    cd ~/TARS
    rm nohup.out
    nohup ./bot.py &
}

send_mail() {
    cat ~/TARS/.pull >>$MAILFILE
    cat $MAILFILE | /usr/sbin/ssmtp ishaqshaik084@gmail.com
}
