function isDateInFuture(dateToCheck) {
  const today = new Date(); // Get the current date and time

  // To compare only by day, month, and year (ignoring time),
  // set the hours, minutes, seconds, and milliseconds to 0 for both dates.
  dateToCheck.setHours(0, 0, 0, 0);
  today.setHours(0, 0, 0, 0);

  // Compare the two dates. If dateToCheck is less than today, it's in the past.
  return dateToCheck >= today;
}

function RefreshOpportunities(sheet) {
	["IN", "PH", "PD"].forEach(function(type) {
		var table = document.getElementById(`opp-table-${type}`).getElementsByTagName('tbody')[0];
		table.innerHTML = ""
		fetch(sheet)
		  .then(res => res.text())
		  .then(tsv => {
			let data = tsv.split("\n").map(r => r.split("\t")).slice(1);
			data.forEach(function(line) {
			  const deadline = new Date(line[1]);
			  if (line[2] == type) {
				  if (line[0] != "" && (isDateInFuture(deadline) || line[1] == "")) {
					  var row = table.insertRow();
					  var cell = row.insertCell();
					  cell.classList.add("position");
					  const newLink = document.createElement('a');
					  newLink.href = line[3];
					  newLink.target = '_blank'; // Optional: opens in a new tab
					  newLink.textContent = line[0];
					  cell.appendChild(newLink)
					  var cell = row.insertCell();
					  cell.classList.add("date");
					  if (line[1] == "") {
						  cell.innerHTML = "⚠️";
					  } else {
						  cell.innerHTML = line[1];
					  }
				  }
			  }

			});
		});
	});
}

document.getElementById("opp-refresh").addEventListener("click", function (e) {
	RefreshOpportunities(this.value);
});
