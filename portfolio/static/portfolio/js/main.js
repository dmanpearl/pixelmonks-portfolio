/* Carousel — track-based push slide (both slides visible during transition) */
(function () {
  const outer = document.getElementById("carousel");
  if (!outer) return;

  const track = document.getElementById("carousel-track");
  const slides = Array.from(outer.querySelectorAll(".carousel-slide"));
  const dots = Array.from(document.querySelectorAll(".carousel-dots .dot"));
  const thumbs = Array.from(document.querySelectorAll(".thumb-strip .thumb"));
  const prevBtn = document.getElementById("carousel-prev");
  const nextBtn = document.getElementById("carousel-next");
  const labelLink = document.getElementById("carousel-label-link");

  let current = 0;
  const total = slides.length;

  function setTrack(index) {
    track.style.transform = `translateX(-${index * 100}%)`;
  }

  function updateLabel(index) {
    if (!labelLink) return;
    const slide = slides[index];
    const slug = slide.dataset.slug;
    const url = slide.dataset.detailUrl;
    labelLink.href = url;
    labelLink.textContent = `open ./projects/${slug}`;
  }

  function updateControls(index) {
    dots.forEach((d, i) => d.classList.toggle("dot--active", i === index));
    thumbs.forEach((t, i) => {
      t.classList.toggle("thumb--active", i === index);
      t.setAttribute("aria-selected", i === index ? "true" : "false");
    });
  }

  function goTo(index) {
    current = ((index % total) + total) % total;
    setTrack(current);
    updateControls(current);
    updateLabel(current);
  }

  // Initialise
  setTrack(0);
  updateLabel(0);

  prevBtn?.addEventListener("click", () => goTo(current - 1));
  nextBtn?.addEventListener("click", () => goTo(current + 1));

  dots.forEach((dot) =>
    dot.addEventListener("click", () => goTo(Number(dot.dataset.target)))
  );
  thumbs.forEach((thumb) =>
    thumb.addEventListener("click", () => goTo(Number(thumb.dataset.target)))
  );

  /* Auto-advance every 6 s; pause on hover */
  let timer = setInterval(() => goTo(current + 1), 6000);
  outer.addEventListener("mouseenter", () => clearInterval(timer));
  outer.addEventListener("mouseleave", () => {
    timer = setInterval(() => goTo(current + 1), 6000);
  });
})();
