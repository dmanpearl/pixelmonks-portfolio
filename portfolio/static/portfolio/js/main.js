/* Generic infinite carousel factory — used for both work and photo carousels */
function makeCarousel({ outerId, trackId, slideClass, prevId, nextId, labelId, dotSelector, thumbSelector, interval }) {
  const outer = document.getElementById(outerId);
  if (!outer) return;

  const track  = document.getElementById(trackId);
  const slides = Array.from(outer.querySelectorAll("." + slideClass));
  const dots   = dotSelector   ? Array.from(document.querySelectorAll(dotSelector))   : [];
  const thumbs = thumbSelector ? Array.from(document.querySelectorAll(thumbSelector)) : [];
  const prevBtn = document.getElementById(prevId);
  const nextBtn = document.getElementById(nextId);
  const labelLink = labelId ? document.getElementById(labelId) : null;

  const total = slides.length;
  if (total === 0) return;

  /* Clone first and last slides for infinite wrap.
     Track layout: [lastClone, slide0 … slideN-1, firstClone] */
  const firstClone = slides[0].cloneNode(true);
  const lastClone  = slides[total - 1].cloneNode(true);
  track.appendChild(firstClone);
  track.insertBefore(lastClone, track.firstChild);

  let current   = 0;   // logical index into real slides[]
  let visualPos = 1;   // position in the extended track
  let locked    = false;

  function moveTo(vi, animated) {
    if (!animated) track.style.transition = "none";
    track.style.transform = `translateX(-${vi * 100}%)`;
    if (!animated) {
      void track.offsetWidth; // flush so transition:none takes effect
      track.style.transition = "";
    }
    visualPos = vi;
  }

  function updateUI() {
    dots.forEach((d, i)  => d.classList.toggle("dot--active", i === current));
    thumbs.forEach((t, i) => {
      t.classList.toggle("thumb--active", i === current);
      t.setAttribute("aria-selected", i === current ? "true" : "false");
    });
    if (!labelLink) return;
    const slide = slides[current];
    if (slide.dataset.detailUrl) labelLink.href = slide.dataset.detailUrl;
    if (slide.dataset.slug) labelLink.textContent = `open ./projects/${slide.dataset.slug}`;
  }

  function goTo(logicalIndex, direct = false) {
    if (locked) return;
    const prev = current;
    current = ((logicalIndex % total) + total) % total;

    if (direct) {
      moveTo(current + 1, true);
    } else if (prev === total - 1 && current === 0) {
      locked = true;
      moveTo(total + 1, true);   // animate into firstClone
    } else if (prev === 0 && current === total - 1) {
      locked = true;
      moveTo(0, true);           // animate into lastClone
    } else {
      moveTo(current + 1, true);
    }
    updateUI();
  }

  /* After animating to a clone, silently snap to the matching real slide */
  track.addEventListener("transitionend", (e) => {
    if (e.propertyName !== "transform") return;
    if (visualPos === total + 1) moveTo(1,     false);  // firstClone → real slide 0
    else if (visualPos === 0)    moveTo(total, false);  // lastClone  → real last slide
    locked = false;
  });

  /* Initialise at real slide 0 */
  moveTo(1, false);
  updateUI();

  prevBtn?.addEventListener("click", () => goTo(current - 1));
  nextBtn?.addEventListener("click", () => goTo(current + 1));

  dots.forEach((dot) =>
    dot.addEventListener("click", () => goTo(Number(dot.dataset.target), true))
  );
  thumbs.forEach((thumb) =>
    thumb.addEventListener("click", () => goTo(Number(thumb.dataset.target), true))
  );

  /* Auto-advance; pause on hover */
  let timer = setInterval(() => goTo(current + 1), interval);
  outer.addEventListener("mouseenter", () => clearInterval(timer));
  outer.addEventListener("mouseleave", () => {
    timer = setInterval(() => goTo(current + 1), interval);
  });
}

/* ── Work / project carousel ── */
makeCarousel({
  outerId:       "carousel",
  trackId:       "carousel-track",
  slideClass:    "carousel-slide",
  prevId:        "carousel-prev",
  nextId:        "carousel-next",
  labelId:       "carousel-label-link",
  dotSelector:   ".carousel-dots .dot",
  thumbSelector: ".thumb-strip .thumb",
  interval:      6000,
});

/* ── About / photo carousel ── */
makeCarousel({
  outerId:       "photo-carousel",
  trackId:       "photo-carousel-track",
  slideClass:    "photo-carousel-slide",
  prevId:        "photo-prev",
  nextId:        "photo-next",
  labelId:       null,
  dotSelector:   null,
  thumbSelector: null,
  interval:      3000,
});
