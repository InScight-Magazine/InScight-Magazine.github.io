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

// async function feedback(vote, permalink) {
// 	console.log(permalink);
//   const response = await fetch(
//     "https://script.google.com/macros/s/AKfycbx_CsR3shAcpSGZPgK52G6NQPuu65EKRHIlxo2G5FVcW7AxqdRAa95D8-JhOIHRZta0/exec",
//     {
//       method: "POST",
//       body: JSON.stringify({
// 		  permalink: permalink,
// 		  vote: vote
//       })
//     }
//   );
// 	if (response.ok) {
//         localStorage.setItem(`voted-$permalink`, "true");
// 		document.getElementById("feedback").style.display = "none";
//     }
// 	console.log(permalink);
//     console.log(await response.text());
// }
//

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
