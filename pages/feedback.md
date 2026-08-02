---
title: "Votes"
permalink: /votes/
---

<button id="votes-summary-button" class="button">Summary</button>
<button id="votes-detailed-button" class="button">Detailed</button>

<table id="votes-summary" style="width: max-content;"></table>
<table id="votes-detailed" style="width: max-content;"></table>

<script src="/assets/js/feedback.js"></script>
<script>
document.getElementById("votes-summary-button").addEventListener('click', () => {
    loadVotes("summary", "{{ site.feedback-db }}", "votes-summary", "votes-detailed");
});
document.getElementById("votes-detailed-button").addEventListener('click', () => {
    loadVotes("detailed", "{{ site.feedback-db }}", "votes-detailed", "votes-summary");
});
loadVotes("summary", "{{ site.feedback-db }}", "votes-summary", "votes-detailed")
</script>
