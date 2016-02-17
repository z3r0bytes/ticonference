#!/bin/bash
clear
echo "--------------------------------------------------------"
echo "Start checking if there are new messages in the database"
echo "Press Ctrl-C to quit"
echo "--------------------------------------------------------"
sleep 3

while [ 1 ]
do
data=$(mysql asterisk --user=root --password=kefjeuh -se "SELECT COUNT(sent) from asterisk.tips WHERE sent = 0")
echo "Er zijn" $data "nieuwe messages"
if [ $data != 0 ]; then
python sms.py
mysql asterisk --user=root --password=kefjeuh -se "UPDATE asterisk.tips SET sent = 1 Where sent = 0"
fi
echo "Done, next occurence in 30 seconds..."
echo ""
sleep 30
echo ""
done
