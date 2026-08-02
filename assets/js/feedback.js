function addEvents(idYes, idNo, permalink) {
	const buttonY = document.getElementById(idYes);
	const buttonN = document.getElementById(idNo);

	buttonY.addEventListener('click', () => {
		feedback(1, permalink);
	});
	buttonN.addEventListener('click', () => {
		feedback(-1, permalink);
	});

	if (localStorage.getItem(`voted-$permalink`) === "true") {
		document.getElementById("feedback").style.display = "none";
	}
}

async function feedback(vote, permalink) {
    const workerURL = "https://website-feedback.scicomm-0e1.workers.dev/";
    const response = await fetch(workerURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            permalink: permalink,
            reaction: vote
        })
    });

    console.log(await response.text());
}

async function loadFeedback() {
  try {
    const response = await fetch(
      "https://website-feedback.scicomm-0e1.workers.dev/api/feedback"
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
      "https://website-feedback.scicomm-0e1.workers.dev/api/summary"
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
