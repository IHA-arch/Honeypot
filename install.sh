#!/bin/bash
root() {
user=`whoami`
if [[ $user != 'root' ]]; then
	echo "Please run as root\n"
	exit
fi
}

check_pakage() {
pakage=`which $pakage_name`
if [[ $pakage == '' ]]; then
	printf "pakage $pakage_name not install\n"
	sleep 0.2
	printf "pakage '$pakage_name' installing...\n"
	apt-get install $pakage_name
else
	sleep 0.5
	printf "pakage installed at '$pakage'\n"
fi
}

root
pakage_name="xterm"
check_pakage
pakage_name="python3"
check_pakage

printf "installing pip3...."
pakage=`which pip3`
if [[ $pakage == '' ]]; then
	printf "installing pip3..."
	apt-get install python3-pip
else
	sleep 0.5
	printf "\npip3 installed at '$pakage'"
fi

sleep 0.5

printf "\ninstall random2....\n"
pip3 install random2


mkdir /usr/share/honeypot_IHA
cp honey.py /usr/share/honeypot_IHA
cp honeypotweb.py /usr/share/honeypot_IHA


access() {
cat > /usr/local/bin/honeypot <<EOF
#!/bin/bash
python3 /usr/share/honeypot_IHA/honey.py
EOF

chmod +x /usr/local/bin/honeypot

printf "\n\ntype 'honeypot' anywhere on the terminal\n"
}
access
