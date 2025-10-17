document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("plannerForm");

  form.addEventListener("submit", (e) => {
    const btn = form.querySelector("button");
    btn.disabled = true;
    btn.textContent = "Planning...";
  });

  // Example: refresh schedule list dynamically
  async function refreshSchedule() {
    try {
      const res = await fetch("/api/schedule");
      const data = await res.json();
      console.log("Current schedule:", data);
    } catch (err) {
      console.error("Failed to fetch schedule", err);
    }
  }

  refreshSchedule();
});
