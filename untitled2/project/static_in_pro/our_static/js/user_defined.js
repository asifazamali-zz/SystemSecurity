    function readTextFile(file,file_path,can_write)
{
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", file, false);
	rawFile.onreadystatechange = function ()
{
	if(rawFile.readyState === 4)
	{
	if(rawFile.status === 200 || rawFile.status == 0)
	{
		var allText = rawFile.responseText;

		document.getElementById('id_message').style.visibility= 'visible';
		document.getElementById('id_filePath').value=file_path;
		document.getElementById("id_message").innerHTML=allText;
		if(can_write=='True')
			document.getElementById('submit').style.visibility='visible';
	}
	}
}
rawFile.send(null);
}