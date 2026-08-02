function addEvents(idYes, idNo, permalink, feedbackdb) {
	console.log(feedbackdb);
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
	if (response.ok) {
		console.log("Okay");
        localStorage.setItem(`voted-${permalink}`, vote);
		document.querySelectorAll("#feedback button").forEach((element, index) => {
			element.style.display = "none";
		});
		document.querySelector('#feedback span').innerHTML = "Your response has been recorded!";
    }
	console.log(localStorage.getItem(`voted-${permalink}`));
    console.log(await response.text());
}

async function loadFeedback() {
  try {
    const response = await fetch(
      `$feedbackdb/api/feedback`
    );

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const rows = await response.json();
    const table = document.getElementById("votes");

    table.innerHTML =
      "<tr><th>Permalink</th><th>Reaction</th><th>Timestamp</th></tr>";

    for (const row of rows) {
      table.innerHTML += `
        <tr>
          <td>${row.permalink}</td>
          <td>${row.reaction}</td>
          <td>${row.timestamp}</td>
        </tr>`;
    }
  } catch (err) {
    console.error("Failed to load feedback:", err);
  }
}


async function loadSummary() {
  try {
    const response = await fetch(
      `$feedbackdb/api/summary`
    );

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const rows = await response.json();
	const table = document.getElementById("votes");

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
  } catch (err) {
    console.error("Failed to load feedback:", err);
  }
}
