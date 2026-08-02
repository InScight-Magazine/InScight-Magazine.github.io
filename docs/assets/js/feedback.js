function addVoteButtonEvents(idYes, idNo, permalink, feedbackdb) {
	const buttonY = document.getElementById(idYes);
	const buttonN = document.getElementById(idNo);

	buttonY.addEventListener('click', () => {
		feedback(1, permalink, feedbackdb);
	});
	buttonN.addEventListener('click', () => {
		feedback(-1, permalink, feedbackdb);
	});

	if (localStorage.getItem(`voted-${permalink}`)) {
		document.querySelectorAll("#feedback button").forEach((element, index) => {
			element.style.display = "none";
		});
		document.querySelector('#feedback span').innerHTML = "Your response has been recorded!";
	}
}

async function feedback(vote, permalink, feedbackdb) {
	document.querySelector('#feedback span').innerHTML = "Recording your response...";
    const response = await fetch(feedbackdb, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            permalink: permalink,
            reaction: vote
        })
    });
	console.log(response);
	if (response.ok) {
		console.log("Okay");
        localStorage.setItem(`voted-${permalink}`, vote);
		document.querySelectorAll("#feedback button").forEach((element, index) => {
			element.style.display = "none";
		});
		document.querySelector('#feedback span').innerHTML = "Your response has been recorded!";
    } else {
		console.log("Not Okay");
		document.querySelector('#feedback span').innerHTML = "Oops, something seems to have gone wrong!";
	}
	console.log(localStorage.getItem(`voted-${permalink}`));
    console.log(await response.text());
}

async function loadVotes(type, feedbackdb, showId, hideId) {
  const url = type == "detailed" ? `${feedbackdb}/api/feedback` : `${feedbackdb}/api/summary`
  console.log(url, type);
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const rows = await response.json();
    const table = document.getElementById(showId);

	document.getElementById(showId).style.display = "block";
	if (type == "detailed") {
		table.innerHTML =
		  "<tr><th>Permalink</th><th>Reaction</th><th>Timestamp</th><th>Region</th></tr>";

		for (const row of rows) {
		  const dateObj = new Date(row.timestamp.replace(" ", "T") + "Z");;
		  table.innerHTML += `
			<tr>
			  <td>${row.permalink}</td>
			  <td>${row.reaction}</td>
			  <td>${dateObj.toLocaleString()}</td>
			  <td>${row.country} - ${row.region}</td>
			</tr>`;
		}
	} else {
		table.innerHTML =
		  "<tr><th>Permalink</th><th>👍</th><th>👎</th></tr>";

		for (const row of rows) {
		  table.innerHTML += `
			<tr>
			  <td>${row.permalink}</td>
			  <td>${row.likes}</td>
			  <td>${row.dislikes}</td>
			</tr>`;
		}
	}
	document.getElementById(hideId).style.display = "none";
  } catch (err) {
    console.error("Failed to load feedback:", err);
  }
}
