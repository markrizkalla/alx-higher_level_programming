$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data, textStatus)
{
			alert("Done, with the following status: " + textStatus + ". Here is the response: " + data);
  $("#character").text(data["name"]);
});
