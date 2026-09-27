(() => {
  const nodes = document.querySelectorAll(".reveal");
  if (nodes.length) {
    if (!("IntersectionObserver" in window)) {
      nodes.forEach((el) => el.classList.add("is-in"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
      );
      nodes.forEach((el) => io.observe(el));
    }
  }

  const storageKey = "shenji-python-checks-v1";

  function loadState() {
    try {
      return JSON.parse(localStorage.getItem(storageKey) || "{}") || {};
    } catch {
      return {};
    }
  }

  function saveState(state) {
    localStorage.setItem(storageKey, JSON.stringify(state));
  }

  function updateProgress(groupName, panel) {
    const boxes = [...panel.querySelectorAll('input[type="checkbox"]')];
    const total = boxes.length;
    const done = boxes.filter((b) => b.checked).length;
    const pct = total ? Math.round((done / total) * 100) : 0;

    const bar = document.querySelector(`[data-progress-for="${groupName}"] .progress-fill`);
    const text = document.querySelector(`[data-progress-text-for="${groupName}"]`);
    if (bar) bar.style.width = `${pct}%`;
    if (text) {
      const unit = groupName.includes("pass") ? "项" : "步";
      text.textContent = `完成 ${done} / ${total} ${unit}`;
    }
  }

  const state = loadState();

  document.querySelectorAll("[data-check-group]").forEach((panel) => {
    const group = panel.getAttribute("data-check-group");
    panel.querySelectorAll('input[type="checkbox"][data-key]').forEach((box) => {
      const key = box.getAttribute("data-key");
      box.checked = Boolean(state[key]);
      box.addEventListener("change", () => {
        const next = loadState();
        next[key] = box.checked;
        saveState(next);
        updateProgress(group, panel);
      });
    });
    updateProgress(group, panel);
  });

  document.querySelectorAll("[data-reset-group]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const group = btn.getAttribute("data-reset-group");
      const panel = document.querySelector(`[data-check-group="${group}"]`);
      if (!panel) return;
      const next = loadState();
      panel.querySelectorAll('input[type="checkbox"][data-key]').forEach((box) => {
        box.checked = false;
        delete next[box.getAttribute("data-key")];
      });
      saveState(next);
      updateProgress(group, panel);
    });
  });
})();
