initialTableContents = null;

/***
 Find the messages with the provided text
*/
function findMessagesWithProvidedText()
{	
	var searchText = $("#searchbox").val();
	var searchTextLowerCase = searchText.toLowerCase();
	if(searchText.length >= 1)
	{
		var contentsTable = document.getElementById("results");
		if(initialTableContents == null)
		{
			initialTableContents = [];
			
			// the first row is header row and skipping it
			for(var rowNum = 1; row = contentsTable.rows[rowNum]; rowNum++)
			{
				var rowContents = {};
				for(var columnNum = 0; cell = row.cells[columnNum]; columnNum++)
				{
					rowContents[contentsTable.rows[0].cells[columnNum].innerHTML] = cell.innerHTML					
				}
				
				initialTableContents.push(rowContents)
			}
		}

		// remove all rows from the table
		$("#results").find("tr:gt(0)").remove();
		
		// search the original contents for matches
		var searchResultsHtml = "";
		for(var itr = 0; itr < initialTableContents.length; itr++)
		{
			var isMatch = false;
			Object.keys(initialTableContents[itr]).forEach(function(key) {
				var contentsLowerCase = initialTableContents[itr][key].toLowerCase();
				if(contentsLowerCase.indexOf(searchTextLowerCase) >= 0)
				{
					isMatch = true;					
				}
			});
			
			if(isMatch)
			{
				rowHtml = "<tr>";
				Object.keys(initialTableContents[itr]).forEach(function(key) {
					rowHtml += "<td>" + initialTableContents[itr][key] + "</td>"
				});
				rowHtml += "</tr>";
				searchResultsHtml += rowHtml;
			}
		}
		
		debugger;
        $("#results tr:last").after(searchResultsHtml);		
	}	
}