initialTableContents = null;

/***
 Find the messages with the provided text
*/
function findMessagesWithProvidedText()
{	
	var searchText = $("#searchbox").val();
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
					if(rowNum == 1)
					{
						alert(cell.innerHTML);
					}
				}
				
				initialTableContents.push(rowContents)
			}
		}

		// remove all rows from the table
		$("#results td").remove();
		for(var itr = 0; itr < initialTableContents.length; itr++)
		{
			
		}			
	}	
}