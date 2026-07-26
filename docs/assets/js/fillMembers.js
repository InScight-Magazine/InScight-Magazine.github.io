async function updateMembers(sheetLink) {
	const data = (await fetch(sheetLink).then(r => r.text())).trim().split("\n");
	const headers = data[0].split("\t");
	const members = data.slice(1);
	const parentNode = document.getElementsByClassName('members')[0];
	for (const i in members) {
		const memberElements = document.getElementsByClassName('member-details');
		const member = members[i]
		const memberDataDict = Object.fromEntries(headers.map((header, j) => [header, member.split("\t")[j]]));
		memberDataDict["email"] = "mailto:" + memberDataDict["email"]
		let element = memberElements[memberElements.length - 1]
		if (memberElements.length < i + 1) {
			element = element.cloneNode(true);
			parentNode.append(element);
		}
		const imgNode = element.querySelector(':scope > img'); 
		imgNode.setAttribute("src", "/" + imgNode.getAttribute("src").split("/").slice(1, -1).join("/") + "/" + memberDataDict["image"]);
		const nameNode = element.querySelector(':scope > strong'); 
		nameNode.innerHTML = memberDataDict["name"];
		const descNode = element.querySelector(".member-desc"); 
		descNode.innerHTML = memberDataDict["desc"];
		const rolesNode = element.querySelector(".member-roles"); 
		rolesNode.innerHTML = memberDataDict["roles"];
		let pastEmail = false;
		for (const [k, v] of Object.entries(memberDataDict)) {
			if (k.toLowerCase() == "email") {
				pastEmail = true;
				element.querySelector("." + k).href = v;
			}
			if (pastEmail == true) {
				console.log(k);
				element.querySelector("." + k).href = v;
			}
		}
	}
	const socials = parentNode.querySelectorAll("a")
	for (ele of socials) {
		if (ele.getAttribute("href").length == 0) {
			ele.remove();
		}
	}
}
