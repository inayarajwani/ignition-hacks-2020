# ignition-hacks-2020


<html>
<body>
<body style="background-color:LightSlateGrey;">

<h1 style="color:LightSlateGrey; "font-family:courier;" >enter</h1>

<h2 style="font-family:courier; color:Ivory; text-align:center; font-size:50px; " > Hello, great to see you again!</h2>

<h3 style="font-family:courier; color:Ivory; text-align:center; font-size:30px; " > Upload you image here </h3>

<p><input type="file"  accept="image/pdf, image/jpg, image/jpeg, image/png" name="image" id="file"  onchange="loadFile(event)" style="display: none;"></p>
<p><label for="file" style="cursor: pointer; font-family:courier; color:Ivory;">Click Me!</label></p>
<p><img id="output" width="500" /></p>

	<script>
		var loadFile = function(event) {
		var image = document.getElementById('output');
		image.src = URL.createObjectURL(event.target.files[0]);
						};
	</script>

</body>

</html>
