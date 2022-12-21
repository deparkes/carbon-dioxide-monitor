while true;
do 
	python3 meter.py
	sudo -E env PATH=$PATH timeout 5s python3 -u -m aioblescan -A | tee test.file  
	python3 ble2db.py
	sleep 300;
done

