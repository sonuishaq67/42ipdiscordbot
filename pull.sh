source ~/TARS/functions.sh
MAILFILE=~/TARS/mail.log
git pull &>.pull
c1=$(cat .pull | grep "up to date" | wc -l)
c2=$(cat .pull | grep "insertion" | wc -l)
c3=$(cat .pull | grep "Aborting" | wc -l)
if [ "$c1" -gt 0 ]; then
    echo "already upto date"
    exit
elif [ "$c2" -gt 0 ]; then
    echo "updating"
    stop_process
    run_again
    echo -e "Subject: Rerun TARS @ $(date)\nTo: ishaqshaik084@gmail.com" >$MAILFILE
    send_mail
elif [ "$c3" -gt 0 ]; then
    echo "error"
    echo -e "Subject: Theres a pulling error for TARS @ $(date)\nTo: ishaqshaik084@gmail.com" >$MAILFILE
    send_mail
fi
