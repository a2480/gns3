<h1>Detection rules engine </h1>
<p>detections rules engine is a project developed in python that allows to automate the management of rules<br> and exceptions in kibana, also capable of generating reports in excel.</p>

<ul><b>Requirements:</b>
<li> - python 3.7</li>
<li> - kibana 7.17.6</li>
</ul>

<ul><b>Python lib requirements:</b>
<li>	requests==2.27.1</li>
<li>	python-dotenv==0.18.0</li>
<li>	numpy==1.16.6</li>
<li>	coverage==5.5</li>
<li>	jsonschema==4.0.0</li>
<li>	pyinstaller==4.1</li>
<li>	click==8.1.3</li>
	<li>pandas==1.1.5</li>
</ul>

<ul><b>Commands:</b>
<li>	clean - clean empty list container in kibana</li>
<ul><li>	-c: specify the client</li></ul>
	<li>deploy - full deployment of detection rules.</li>
<ul><li>	-c: specify the client</li></ul>
	<li>forcedelete - remove all Detection rules existing in Kibana but not in...</li>
	<li>report - specifies the teste  deadline for inclusion of temporary exceptions.</li>
<ul><li>	-c: specify the client</li></ul>
<ul><li>	-t: specify the limit of time to include deleted exceptions</li></ul>
	<li>tdelete - Temporary exceptions delete of clients</li>
<li>testdetections - Run a full test of detection rules</li>
<ul><li>	o	-c: specify the client</li></ul>

</ul>
<br>
<b>Examples:</b><br>
python DetectionRulesEngine.py –help<br>
python DetectionRulesEngine.py deploy<br>
python DetectionRulesEngine.py deploy -c vic<br>
python DetectionRulesEngine.py forcedelete<br>
